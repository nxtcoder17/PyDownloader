import os
import sys
import subprocess
from multiprocessing import Lock
import shutil
# import threading

import requests

from libs.SpawnProcesses import MyProcess
from libs.ParseUrl import ParseUrl
from libs.TaskQueue import generate_queue, singleton_queue
from libs.ProgressBar import ProgressBar

class PyDownloader:
    """ A wrapper to all download related information and perform downloads"""
    def __init__(self, url, name):
        self.url = url
        self.dump_dir = '.' + name
        self.chunk_size = 64 * 1024         # Write these many bytes at a time
        self.content_length = ParseUrl(url).extract_info()['content-length']

        # Requests Session
        self.session = requests.Session()
        self.session.headers.update({'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'})

        if self.content_length is None:
            # Content-Length Header Unknown, can't multi process the download, 
            # then doing it the old-school way
            self.que = singleton_queue()
            os.mkdir(self.dump_dir)
        else:
            try:
                os.mkdir(self.dump_dir)
                self.que = generate_queue(2*1024*1024, self.content_length, None)
            except FileExistsError:
                offsets = self.fix_already_downloaded()
                self.que = generate_queue(2*1024*1024, self.content_length, offsets)

        self.lock = Lock()

        self.processes = []
        for i in range(3):
            t = MyProcess(name="Process-" + str(i), handler=self.handler)
            t.start()
            self.processes.append(t)

        # I also sort of need a ProgressBar
        # I will do so, with a Daemon Thread
        progress_bar = ProgressBar(self.dump_dir, self.content_length)
        progress_bar.setDaemon(True)
        progress_bar.start()

        for process in self.processes:
            process.join()

        with open(name, "wb") as f:
            for file in sorted(map(int, os.listdir(self.dump_dir))):
                with open(self.dump_dir + f'/{file}', 'rb') as r:
                    f.write(r.read())
            subprocess.call(['notify-send', f'Download Complete: {name}'])
        shutil.rmtree(self.dump_dir)

    def handler(self, name):
        while True:
            while not self.que.empty():
                self.lock.acquire()
                item = self.que.get(block = False)
                self.lock.release()
                # print(f"[THREAD] {name}: popped {item} from QUEUE")

                self.worker(item)
            else:
                return 

    def worker(self, item):
        response = self.session.get(self.url, stream=True, headers = item[-1])
        with open(f"{self.dump_dir}/{item[0]}", 'ab') as f:
            for data in response.iter_content(chunk_size = self.chunk_size):
                try:
                    pass
                except KeyboardInterrupt:
                    pass
                finally:
                    f.write(data)
                    # print("Yeah! It is working!!!!!!!!!!!!!!!!!!!!!!!!!")

    def fix_already_downloaded(self):
        d = dict()
        for file in os.listdir(self.dump_dir):
            d[int(file)] = os.path.getsize(f'{self.dump_dir}/{file}')
        return d

if __name__ == '__main__':
    p = PyDownloader(sys.argv[1], sys.argv[2])

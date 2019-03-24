import os
import sys
import requests
from multiprocessing import Lock
import threading
from libs.SpawnProcesses import MyProcess
from libs.ParseUrl import ParseUrl
from libs.TaskQueue import generate_queue
from libs.ProgressBar import ProgressBar

class PyDownloader:
    def __init__(self, url, name):
        self.url = url
        self.dump_dir = '.' + name
        self.chunk_size = 64 * 1024         # Write these bytes at a time
        self.content_length = ParseUrl(url).extract_info()['content-length']

        try:
            os.mkdir(self.dump_dir)
            self.que = generate_queue(2*1024*1024, self.content_length, None)
        except FileExistsError:
            offsets = self.fix_already_downloaded()
            self.que = generate_queue(2*1024*1024, self.content_length, offsets)

        # flag = False
        # try:
            # os.mkdir(self.dump_dir)
            # self.que, list = TaskQueue(2*1024*1024, self.content_length).generate()
        # except FileExistsError:
            # flag = True
            # # Already downloaded part
            # # parse already downloaded parts and fix the issue WITHIN Existing QUEUE
            # offsets = self.fix_already_downloaded()
        # 
            # self.que, list = TaskQueue(2*1024*1024, self.content_length).generate(offsets)
        # self.que = TaskGenerator(2*1024*1024, self.content_length).generate()
        # self.que = generat_queue(2*1024*1024, self.content_length, offsets)

        # print(f"[Size of que: {len(self.que)})

        self.lock = Lock()

        self.processes = []
        for i in range(3):
            t = MyProcess(name = "Process-" + str(i), handler=self.handler)
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

    def handler(self, name):
        while True:
            while not self.que.empty():
                self.lock.acquire()
                item = self.que.get(block = False)
                self.lock.release()
                print(f"[THREAD] {name}: popped {item} from QUEUE")

                self.worker(item)
            else:
                return 

    def worker(self, item):
        response = requests.get(self.url, stream=True, headers = item[-1])
        with open(f"{self.dump_dir}/{item[0]}", 'ab') as f:
            for data in response.iter_content(chunk_size = self.chunk_size):
                try:
                    pass
                except KeyboardInterrupt:
                    pass
                    # offset = os.path.getsize(f"{self.dump_dir}/{file}") % self.chunk_size
                    # os.ftruncate(f.fileno(), f.seek(0, 2) - offset);
                    # f.write(data)
                    # f.close();
                    # print("You Know, it is actually working !!!!!!!")
                    # raise KeyboardInterrupt
                finally:
                    f.write(data)
                    # print("Yeah! It is working!!!!!!!!!!!!!!!!!!!!!!!!!")

    def fix_already_downloaded(self):
        d = dict()
        for file in os.listdir(self.dump_dir):
            d[int(file)] = os.path.getsize(f'{self.dump_dir}/{file}')
        return d

p = PyDownloader(sys.argv[1], sys.argv[2])

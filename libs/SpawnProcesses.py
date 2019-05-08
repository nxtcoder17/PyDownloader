import multiprocessing


lock = multiprocessing.Lock()

class MyProcess(multiprocessing.Process):
    def __init__(self, name, handler):
        multiprocessing.Process.__init__(self)
        self.name = name
        self.handler = handler

    def run(self):
        lock.acquire()
        # print(f"Starting PROCESS {self.name}")
        lock.release()

        # call to a handler function
        self.handler(self.name)

        lock.acquire()
        # print(f"Finishing PROCESS {self.name}")
        lock.release()




import os
import time
import threading
from .ColorPython import Color

class ProgressBar(threading.Thread):
    def __init__(self, dir, total):
        threading.Thread.__init__(self)
        self.dir = dir
        self.total = total

    def run(self):
        generate(self.dir, self.total)

# pprint aka pretty_print method
pprint = lambda x, y: Color.bold[x] + y + Color.neutral

def generate(dir, total):
    size = lambda : sum(os.path.getsize(dir + '/' + x) for x in os.listdir(dir))

    print ("[" + pprint("green", "Download-Size") + "]: " + pprint("yellow", "{:.2f} MBs".format(total/1024/1024)))
    while True:
        result = "["
        if total is not None:
            percentage = (size()/total) * 100
            result += pprint("green", f"{'#' * int(percentage // 2)}")
            result += pprint("cyan", f"{'.' * int(50 - (percentage // 2))}")
            result += "]"

            if size() != total:
                result += "({:3.2f} %) ({:4.2f} MB) ".format(percentage, size()/1024/1024)
            elif (size() == total):
                result += "(100.00 %)"
        else:
            result += pprint ("green", f"{'#' * 50}")
            result += "]"
            result += " (Undetermined) ({:4.2f} MB)".format (size()/1024/1024);
        # result += "#" * int(percentage // 2) + "." * int(50 - (percentage // 2))
        print(result, end='\r')
        time.sleep(0.1)

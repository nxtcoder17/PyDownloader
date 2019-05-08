from multiprocessing import Queue

def singleton_queue ():
    que = Queue()
    que.put ((0, {'range': f"bytes=0-"}))
    return que

def generate_queue(unit, total, offsets = None):
    # self.que.put((counter, {'range': f"bytes={start+offsets[counter]}-{start + self.unit - 1}" }))
    que = Queue()

    start = 0
    end = total - 1

    counter = 1

    while (start + unit <= end):
        # print(f"[SHOULD BE]: range: bytes={start}-{start + unit - 1}")
        if offsets is not None:
            offsets[counter] = 0 if counter not in offsets else offsets[counter]
            if (start + offsets[counter] <= (start + unit - 1)):
                que.put((counter, {'range': f"bytes={start + offsets[counter]}-{start + unit - 1}"}))
                # print(f"\t[OFFSET]: {offsets[counter]}")
                # print(f"[ CURRENT ]: range: bytes={start + offsets[counter]}-{start + unit - 1}")
                # print()
        else:
            que.put((counter, {'range': f"bytes={start}-{start + unit - 1}"}))
            # print(f"[ CURRENT ]: range: bytes={start}-{start + unit - 1}")
            print()

        start += unit
        counter += 1

    if (start + unit > end):
        # print(f"[SHOULD BE]: range: bytes={start}-{end}")
        if offsets is not None:
            offsets[counter] = 0 if counter not in offsets else offsets[counter]
            if (start + offsets[counter] <= end):
                que.put((counter, {'range': f"bytes={start + offsets[counter]}-{end}"}))
                # print(f"\t[OFFSET]: {offsets[counter]}")
                # print(f"[ CURRENT ]: range: bytes={start + offsets[counter]}-{end}")
        else:
            que.put((counter, {'range': f"bytes={start}-{end}"}))
            # print(f"[ CURRENT ]: range: bytes={start}-{end}")
            # print()

    return que


# class TaskQueue:
    # def __init__(self, unit, total):
        # # Contents of my queue would be tuples
        # # each tuple be like, 
        # #           (counter, header)
        # # each header be like a dict(), like
        # #               {'range': 'bytes={start}-{end}'}
        # self.que = Queue()
        # self.list = []
        # self.unit = unit
        # self.total = total
# 
    # def generate(self, offsets = None):
        # start = 0
        # end = self.total -1
# 
        # counter = 1
        # while (start + self.unit <= end):
            # print(f"[SHOULD BE]: \trange: bytes={start} - {start + self.unit - 1}")
            # ###
            # if offsets is not None and counter in offsets and ((start+self.unit-1)-start+1) != offsets[counter]:
                # print(f"[CURRENT]: \t{range: bytes={start + offsets[counter]} - {start + self.unit - 1}")
                # self.que.put((counter, {'range': f"bytes={start+offsets[counter]}-{start + self.unit - 1}" }))
                # self.list.append((counter, {'range': f"bytes={start+offsets[counter]}-{start + self.unit - 1}" }))
            # ###
            # else:
                # print(f"[CURRENT]: \t{range: bytes={start + 
                # self.que.put((counter, {'range': f"bytes={start}-{start + self.unit - 1}"}))
                # self.list.append((counter, {'range': f"bytes={start}-{start + self.unit - 1}"}))
            # start = start + self.unit
            # counter += 1
# 
        # if (start + self.unit > end):
            # if offsets is not None and counter in offsets and ((end)-start+1) != offsets[counter]:
                # self.que.put((counter, {'range': f"bytes={start+offsets[counter]}-{end}"}))
                # self.list.append((counter, {'range': f"bytes={start+offsets[counter]}-{end}"}))
            # else:
                # self.que.put((counter, {'range': f"bytes={start}-{end}"}))
                # self.list.append((counter, {'range': f"bytes={start}-{end}"}))
# 
        # return self.que, self.list

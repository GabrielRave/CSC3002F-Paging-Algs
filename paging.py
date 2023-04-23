# Gabriel Ravenscroft RVNGAB001
# Assignment 3 CSC3002F
# A program to implement different page replacement algorithms

import sys
import random
import queue



def OPT(size, original_pages):
    pages = original_pages.copy()       # make a duplicate of pages to be used in method
    faults = 0
    q = queue.Queue()   # q (queue) represents main memory
    while len(pages) != 0:
        x = pages[0]
        done = False

        for i in list(q.queue):  # loop used to check if page to be added to memory is already in memory (queue)
            if i == x:
                done = True

        if not done and q.qsize() == size:  # Case of page fault. page is not in mem (queue: q) and mem is full
            last = -1
            pageToReplace = -1
            for j in list(q.queue):
                if pages.count(j) != 0:
                    nextUse = pages.index(j)
                    if nextUse > last:
                        pageToReplace = j
                        last = nextUse
                else:
                    pageToReplace = j
                    last = 99999

            for y in range(q.qsize()):  
                current_element = q.get()
                if current_element != pageToReplace:
                    q.put(current_element)
            q.put(x)        # x (the newest page) added onto head of queue
            faults = faults + 1

        if not done and q.qsize() < size:  # Case in which memory (queue: q) still has space for a page to be added
            q.put(x)
        pages.pop(0)
    return faults


def LRU(size, original_pages):
    pages = original_pages.copy()       # make a duplicate of pages to be used in method
    faults = 0
    q = queue.Queue()  # q (queue) represents main memory
    while len(pages) != 0:
        x = pages[0]
        done = False
        for i in list(q.queue):  # loop used to check if page to be added to memory is already in memory (queue)
            if i == x:
                for y in range(q.qsize()):  # loop removes copy of x (newest page) from queue
                    current_element = q.get()
                    if current_element != x:
                        q.put(current_element)
                q.put(x)  # x (the newest page) added onto head of queue
                done = True

        if not done and q.qsize() == size:  # Case of page fault is page is not in mem (queue: q) and mem is full
            q.get()
            q.put(x)
            faults = faults + 1

        if not done and q.qsize() < size:  # Case in which memory (queue: q) still has space for a page to be added
            q.put(x)
        pages.pop(0)
    return faults


def FIFO(size, original_pages):
    pages = original_pages.copy()       # make a duplicate of pages to be used in method
    faults = 0
    q = queue.Queue()  # q (queue) represents main memory
    while len(pages) != 0:
        x = pages[0]
        done = False
        for i in list(q.queue):  # loop used to check if page to be added to memory is already in memory (queue)
            if i == x:
                done = True

        if not done and q.qsize() == size:  # Case of page fault is page is not in memory (queue: q) and is full
            q.get()
            q.put(x)
            faults = faults + 1

        if not done and q.qsize() < size:  # Case in which memory (queue: q) still has space for a page to be added
            q.put(x)
        pages.pop(0)
    return faults

def main():
    size = 5  # number of slots in main memory
    length = 20  # number of input pages that will need to be put on main memory
    pages = []
    for j in range(length):
        pages.append(random.randint(1, 9))
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    print("FIFO", FIFO(size, pages), "page faults.")
    print("LRU", LRU(size, pages), "page faults.")
    print("OPT", OPT(size, pages), "page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of page frames]")
        main() #remove this!!
    else:
        main()

# print("FIFO", FIFO(size, FIFO_pages), "page faults.")
# print("LRU", LRU(size, LRU_pages), "page faults.")
# print("OPT", OPT(size, OPT_pages), "page faults.")

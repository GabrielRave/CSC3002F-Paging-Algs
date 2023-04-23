# Gabriel Ravenscroft RVNGAB001
# Assignment 3 CSC3002F 2023
# A program to implement different page replacement algorithms

import sys
import random
import queue


def OPT(size, original_pages):
    pages = original_pages.copy()  # make a duplicate of pages to be used in method
    faults = 0
    q = queue.Queue()  # q (queue) represents main memory

    while len(pages) != 0:  # loop while there are pages that need to be put into memory
        x = pages.pop(0)  # x is page to be added to main memory (q)
        done = False

        # Case 1
        for i in list(q.queue):  # Case in which next page to be added is already in memory (queue)
            if i == x:
                done = True

        # Case 2
        if not done and q.qsize() < size:  # Case in which memory (queue: q) still has space for a page to be added
            q.put(x)

        # Case 3
        elif not done and q.qsize() == size:  # Case of page fault. page is not in mem (queue: q) and mem is full
            last = -1
            page_to_replace = None      # This will be the page in queue that either reappears last or does not reappear

            for j in q.queue:  # loop finds page_to_replace. page_to_replace will always be found
                if j not in pages:  # case in which there is element of main memory (q) that is not in pages
                    page_to_replace = j
                    break

                elif pages.index(j) > last:  # find element of q that will be needed again furthest in future
                    last = pages.index(j)
                    page_to_replace = j

            for y in range(q.qsize()):      # remove page_to_replace from queue
                current_element = q.get()
                if current_element != page_to_replace:
                    q.put(current_element)
            q.put(x)  # add x (the newest page) added onto head of queue
            faults = faults + 1
    return faults


def LRU(size, original_pages):
    pages = original_pages.copy()  # make a duplicate of pages to be used in method
    faults = 0
    q = queue.Queue()  # q (queue) represents main memory
    while len(pages) != 0:  # loop while there are pages that need to be put into memory
        x = pages.pop(0)
        done = False

        # Case 1
        for i in list(q.queue):  # Case in which next page to be added is already in memory (queue)
            if i == x:  # if page to be added to memory is already in memory (queue)
                for y in range(q.qsize()):  # loop removes old copy of x (newest page) from queue
                    current_element = q.get()
                    if current_element != x:
                        q.put(current_element)
                q.put(x)  # x (the newest page) added onto head of queue
                done = True

        # Case 2
        if not done and q.qsize() < size:  # Case in which memory (queue: q) still has space for a page to be added
            q.put(x)

        # Case 3
        elif not done and q.qsize() == size:  # Case of page fault. Page is not in mem (queue: q) and mem is full
            q.get()
            q.put(x)
            faults = faults + 1
    return faults


def FIFO(size, original_pages):
    pages = original_pages.copy()  # make a duplicate of pages to be used in method
    faults = 0
    q = queue.Queue()  # q (queue) represents main memory
    while len(pages) != 0:  # loop while there are pages that need to be put into memory
        x = pages.pop(0)
        done = False

        # Case 1
        for i in list(q.queue):  # Case in which next page to be added is already in memory (queue)
            if i == x:
                done = True

        # Case 2
        if not done and q.qsize() < size:  # Case in which memory (queue: q) still has space for a page to be added
            q.put(x)

        # Case 3
        elif not done and q.qsize() == size:  # Case of page fault is page is not in memory (queue: q) and is full
            q.get()
            q.put(x)
            faults = faults + 1
    return faults


def main():
    length = 20  # number of input pages that will need to be put on main memory
    size = int(sys.argv[1])     # number of slots in main memory
    pages = []
    for j in range(length):
        pages.append(random.randint(1, 9))
    print("FIFO", FIFO(size, pages), "page faults.")
    print("LRU", LRU(size, pages), "page faults.")
    print("OPT", OPT(size, pages), "page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of page frames]")
    else:
        main()

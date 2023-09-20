import heapq
import sys
input = sys.stdin.readline

n = int(input())

lheap = []
rheap = []

for i in range(n):
    num = int(input())

    if i % 2 == 0:
        heapq.heappush(lheap, -num)
    
    else:
        heapq.heappush(rheap, num)

    if i > 0:    
        if -lheap[0] > rheap[0]:
            l = heapq.heappop(lheap)
            r = heapq.heappop(rheap)

            heapq.heappush(lheap, -r)
            heapq.heappush(rheap, -l)

    print("result: ", -lheap[0])

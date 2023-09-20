import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0:
        if len(heap) > 0:
            print(-heap[0])
            heapq.heappop(heap)

        else:
            print(-1)

    else:
        for i in range(1, len(a)):
            heapq.heappush(heap, -a[i])

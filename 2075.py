import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = list(map(int, input().split()))
    for n in num:
        if len(heap) < N:
            heapq.heappush(heap, n)
        else:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

print(heap[0])

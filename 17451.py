import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))

min = v[-1]

for i in range(n-2, -1, -1):
    if min < v[i]:
        min = v[i]
    else:
        if min % v[i]:
            min = (min//v[i]+1) *v[i]

print(min)

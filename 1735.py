import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

A = a*d + b*c
B = b*d

M = max(A, B)
m = min(A, B)

while(m):
    M %= m
    M, m = m, M

print(A//M, B//M)

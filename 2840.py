import sys
input = sys.stdin.readline

N, K = map(int, input().split())

wheel = ['?']*N
alpa = [0]*26
n = 0
T = True

for i in range(K):
    num, l = input().split()
    n = (n + int(num))%N

    if wheel[n] == '?':
        wheel[n] = l
    
    else:
        if wheel[n] != l:
            T = False

word = wheel[n+1:] + wheel[:n+1]

for i in range(N):
    if word[i] != '?':
        alpa[ord(word[i])-65] += 1

for i in range(26):
    if alpa[i] > 1:
        T = False

if not T:
    print('!')

else:
    for i in range(N):
        print(word[N-1-i], end = '')

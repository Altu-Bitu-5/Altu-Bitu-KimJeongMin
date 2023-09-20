import sys
input = sys.stdin.readline

N = int(input())
result = 0

word = input()
alpa = [0]*26

for i in range(len(word)-1):
    alpa[ord(word[i])-ord('A')] += 1 

for _ in range(N-1):
    ow = input()
    oa = [0]*26
    cnt = 0

    for i in range(len(ow)-1):
        oa[ord(ow[i])-ord('A')] += 1

    for i in range(26):
        if alpa[i] != oa[i]:
            cnt += abs(alpa[i] - oa[i])
            
    
    if len(word) == len(ow):
        if cnt == 0 or cnt == 2:
            result +=1

    else:
        if cnt == 1 and abs(len(word) - len(ow)) == 1:
            result += 1

print(result)

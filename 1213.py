import sys
input = sys.stdin.readline


name = input()
palinL = []

alpha = [0]*26

odd = 0
center = 'A'

for i in range(len(name)):
    alpha[ord(name[i])-ord('A')] += 1

for i in range(26):
    if alpha[i]%2 != 0:
        odd += 1

if odd>1:
    print("I'm Sorry Hansoo")

else:
    for i in range(26):
        if alpha[i] != 0:
            for j in range(alpha[i]//2):
                palinL.append(chr(i+ord('A')))
            
            if alpha[i]%2 == 1:
                center = chr(i+ord('A'))
    palinR = list(reversed(palinL))

    newpalL = ''.join(map(str, palinL))
    newpalR = ''.join(map(str, palinR))

    if odd == 0:
        print(newpalL, end='')
        print(newpalR)

    else:
        print(newpalL, end='')
        print(center, end = '')
        print(newpalR)    

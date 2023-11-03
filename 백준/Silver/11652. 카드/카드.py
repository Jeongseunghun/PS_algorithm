import sys
input = sys.stdin.readline

N = int(input())
dict = {}
for i in range(N):
    card = int(input())
    if card not in dict:
        dict[card] = 1
    else:
        dict[card] +=1

dict = sorted(dict.items(),key = lambda x : (-x[1],x[0]))

print(dict[0][0])
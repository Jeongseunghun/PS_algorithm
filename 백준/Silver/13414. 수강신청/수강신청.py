import sys
input = sys.stdin.readline

K,L = map(int,input().split())
lst = {}
for i in range(1,L+1):
    id = input().rstrip()
    if id not in lst:
        lst[id] = i
    else:
        lst[id] = i

lst = sorted(lst.items(),key = lambda x : x[1])

if(K>len(lst)):
    K = len(lst)

for i in range(K):
    print(lst[i][0])
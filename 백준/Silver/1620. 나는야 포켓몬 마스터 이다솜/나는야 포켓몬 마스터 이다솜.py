import sys

input = sys.stdin.readline

N,M = map(int,input().split())
dict = {}
for i in range(1,N+1):
    name = input().strip()
    dict[i] = name
    dict[name] = i
    
for i in range(M):
    tmp = input().strip()
    if tmp.isdigit():
        print(dict[int(tmp)])
    else:
        print(dict[tmp])
    
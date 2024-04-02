import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

name = []
for _ in range(N):
    n,c = input().split()
    name.append((n,int(c)))

for _ in range(M):
    hp = int(input())
    s = 0
    e = N-1
    while s<=e:
        mid = (s+e) // 2
        if name[mid][1] < hp:
            s = mid+1
        else:
            e = mid-1
    print(name[s][0])
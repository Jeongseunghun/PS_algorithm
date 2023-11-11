N = int(input())
lst = []
for i in range(N):
    x,y = map(int,input().split())
    lst.append((x,y))

lst.sort()

for i in lst:
    print(*i)
N = int(input())
lst = []
for i in range(N):
    a,b = map(int,input().split())
    lst.append([a,b])

lst = sorted(lst,key = lambda x: (x[1],x[0]))

for i in lst:
    print(*i)
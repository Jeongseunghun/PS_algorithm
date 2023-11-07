N = int(input())
lst = []
for i in range(N):
    name,k,e,m = map(str,input().split())
    lst.append([name,int(k),int(e),int(m)])

lst = sorted(lst,key = lambda x : (-x[1],x[2],-x[3],x[0]))

for i in lst:
    print(i[0])
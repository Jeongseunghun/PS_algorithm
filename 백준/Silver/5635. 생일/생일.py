N = int(input())
lst = []
for _ in range(N):
    n,d,m,y = input().split()
    lst.append([int(y),int(m),int(d),n])

lst = sorted(lst,key = lambda x : (x[0],x[1],x[2]))

print(lst[-1][3])
print(lst[0][3])
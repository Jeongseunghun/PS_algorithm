from re import L


N=int(input())
num=str(input())
a=list(num)

cnt=0
for i in range(len(a)):
    cnt+=int(a[i])

print(cnt)

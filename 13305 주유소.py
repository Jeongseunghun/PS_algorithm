N = int(input())
length = list(map(int,input().split()))
price = list(map(int,input().split()))

res=0
m=price[0]
for i in range(N-1):
    if price[i]<m:
        m=price[i]
    res+=m*length[i]

print(res)
N=int(input())
price=[]
res=0

for _ in range(N):
    price.append(int(input()))

price.sort(reverse=True)

for i in range(N):
    if i% 3 != 2 :
        res+= price[i]

print(res)
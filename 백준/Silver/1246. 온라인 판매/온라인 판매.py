N,M = map(int,input().split())
lst = [int(input()) for _ in range(M)]

lst.sort()

price = 0
profit = 0

for i in range(M):
    e = min(M-i, N)
    
    if price < lst[i] * e:
        price = lst[i] * e
        profit = lst[i]

print(profit,price)
    
N, K = map(int,input().split())
money=[]
cnt = 0

for i in range(N):
    money.append(int(input()))

money.sort(reverse=True)

for i in range(len(money)):
    if money[i]<=K:
       cnt += K // money[i]
       K = K % money[i]
       

print(cnt)
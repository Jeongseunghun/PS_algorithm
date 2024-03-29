N = int(input())

ans = 1
while N > 0:
    ans*=N
    N-=1

ans = str(ans)

res = 0
for i in range(len(ans)-1,-1,-1):
    if ans[i] == '0':
        res+=1
    else:
        break

print(res)
N = input()
a = N.count('a')

N += N
ans = 1e9
for i in range(len(N)-a+1):
    ans = min(ans,N[i:i+a].count('b'))

print(ans)
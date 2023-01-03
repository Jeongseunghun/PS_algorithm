N = int(input())

res = 0

for i in range(1,N+1):
    i_sum = list(map(int,str(i)))
    if N == i + sum(i_sum):
        ans = i
        print(ans)
        break
    if N == i:
        print(0)
    
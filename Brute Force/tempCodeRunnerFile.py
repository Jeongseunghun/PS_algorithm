N = int(input())

res = [i for i in range(N)]

for i in range(len(res)):
    i_sum = list(map(int,str(res[i])))
    if N == res[i] + sum(i_sum):
        ans = res[i]
        print(ans)
        break
    
    
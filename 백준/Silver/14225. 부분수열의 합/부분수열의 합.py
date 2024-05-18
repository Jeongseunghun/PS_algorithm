def fill(cnt,a):
    if cnt == N:
        lst[a] = 1
        return
    fill(cnt+1,a)
    fill(cnt+1,a+S[cnt])

N = int(input())
S = list(map(int,input().split()))

lst = [0] * 2000000
fill(0,0)
for i in range(len(lst)):
    if lst[i] == 0:
        print(i)
        break

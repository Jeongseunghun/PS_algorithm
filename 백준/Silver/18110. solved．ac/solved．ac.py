import sys
input = sys.stdin.readline

def my_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
erase = my_round(n*0.15)

if n ==0:
    print(0)
else:
    res = 0
    cnt = 0
    for i in range(erase,n-erase):
        res+=lst[i]
        cnt+=1

    ans = my_round(res/cnt)

    print(ans)
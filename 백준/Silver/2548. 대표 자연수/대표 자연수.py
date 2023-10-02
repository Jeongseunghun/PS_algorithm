N = int(input())
num = list(map(int,input().split()))
num.sort()

l,r = divmod(N,2)

print(num[l+r-1])
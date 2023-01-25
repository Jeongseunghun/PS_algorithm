T = int(input())
for i in range(T):
    lst = list(map(int,input().split()))
    lst.sort()
    print(lst[-3])
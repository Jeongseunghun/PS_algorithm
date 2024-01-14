n = int(input())
A = list(map(str,input().split()))
dict = {}
for i in A:
    dict[i] = 0
for i in range(n):
    lst = list(map(str,input().split()))
    for j in lst:
        dict[j] +=1

dict = sorted(dict.items(),key = lambda x : (-x[1],x[0]))
for i in range(n):
    print(dict[i][0],dict[i][1])
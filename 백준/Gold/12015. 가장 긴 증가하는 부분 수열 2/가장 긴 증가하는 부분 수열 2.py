from bisect import bisect_left

N = int(input())
lst = list(map(int,input().split()))

l = [lst[0]]

for i in lst:
    if l[-1] < i:
        l.append(i)
    else:
        idx = bisect_left(l,i)
        l[idx] = i
    
print(len(l))
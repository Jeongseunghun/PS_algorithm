# N = int(input())
# lst = list(map(int,input().split()))

# print(min(lst),max(lst))

N = int(input())
lst = list(map(int,input().split()))

max = lst[0]
min = lst[0] 
for i in lst:
    if i >= max:
        max = i
    if i <= min:
        min = i
        
print(min,max)
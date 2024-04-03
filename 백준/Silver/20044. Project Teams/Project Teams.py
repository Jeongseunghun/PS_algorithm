n = int(input())
lst = list(map(int,input().split()))
lst.sort()

minVal = 1e9
for i in range(n):
    minVal = min(lst[i] + lst[-1-i],minVal)

print(minVal)
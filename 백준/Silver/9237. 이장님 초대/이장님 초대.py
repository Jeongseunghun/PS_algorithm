N = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)

day = 0

for i in range(N):
    day = max(day,lst[i]+i)
    
print(day+2)
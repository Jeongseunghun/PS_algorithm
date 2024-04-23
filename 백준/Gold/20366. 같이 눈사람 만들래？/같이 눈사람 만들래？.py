N = int(input())
lst = list(map(int,input().split()))
lst.sort()

ans = 1e9
for i in range(N-3):
    for j in range(i+3,N):
        tmp = lst[i] + lst[j]
        l,r = i+1,j-1
        
        while l < r:
            s = lst[l] + lst[r]
            if abs(s-tmp) < ans:
                ans = abs(s-tmp)
            
            if s < tmp:
                l+=1
            elif s > tmp:
                r-=1
            else:
                print(0)
                exit()

print(ans)
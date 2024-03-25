N,C = map(int,input().split())
house = [int(input()) for _ in range(N)]
house.sort()

ans = 0
#최소거리
s = 1
#최대거리
e = house[-1] - house[0]

def binary_search(s,e):
    while s<=e:
        mid = (s+e)//2
        cnt = 1
        current = house[0]
        
        for i in range(1,N):
            if house[i] >= mid+current:
                cnt+=1
                current = house[i]
                
        if cnt >= C:
            global ans
            s = mid+1
            ans = mid
        else:
            e = mid - 1


binary_search(s,e)

print(ans)
T = int(input())
for i in range(T):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    #-7, -4, -3, -2, 0, 1, 2, 5, 9, 12
    lst.sort()
    #K와 가장 가까운 두 정수 구하기
    l = 0
    r = N-1
    ans = 0
    dis = 1e9
    while l < r:
        tmp = abs(K-(lst[l]+lst[r]))
        #갱신
        if tmp < dis:
            ans = 1
            dis = tmp
            if K-(lst[l]+lst[r]) < 0:
                r-=1
            else:
                l+=1
        elif tmp == dis:
            ans+=1
            if K-(lst[l]+lst[r]) < 0:
                r-=1
            else:
                l+=1
        else:
            if K-(lst[l]+lst[r]) < 0:
                r-=1
            else:
                l+=1
                
            
    print(ans)
N,new,P = map(int,input().split())
if N == 0:
    print(1)
else:
    ranking = list(map(int,input().split()))
    if new <= ranking[-1] and N == P:
        print(-1)
    else:
        ans = N+1
        for i in range(N):
            if ranking[i] <= new:
                ans = i+1
                break
        print(ans)       
        
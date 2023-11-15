T = int(input())
for i in range(T):
    cnt = 0
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    
    s = 0
    cnt = 0
    for j in range(N):
        while True:
            if s == M or A[j] <= B[s]:
                cnt += s
                break
            else:
                s +=1
    
    print(cnt)

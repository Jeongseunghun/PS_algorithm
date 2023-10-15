from collections import deque

N,M,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

cnt = min(N,M) // 2
q = deque()
for i in range(cnt):
    q.clear()
    #위
    q.extend(A[i][i:M-i])
    #오
    q.extend([A[j][M-i-1] for j in range(i+1,N-i-1)])
    #아래
    q.extend(A[N-i-1][i:M-i][::-1])
    #왼
    q.extend([A[j][i] for j in range(i+1,N-i-1)][::-1])
    
    #반시계 회전
    q.rotate(-R)
    
    #위
    for j in range(i,M-i):
        A[i][j] = q.popleft()
    
    #오
    for j in range(i+1,N-i-1):
        A[j][M-i-1] = q.popleft()
    
    #아래
    for j in range(M-i-1,i-1,-1):
        A[N-i-1][j] = q.popleft()
    
    #왼
    for j in range(N-i-2,i,-1):
        A[j][i] = q.popleft()
        
for i in range(N):   
    print(*A[i])
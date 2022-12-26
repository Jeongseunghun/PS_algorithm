import sys
input = sys.stdin.readline

T = int(input())
a=[]
for _ in range(T):
    N=int(input())
    for _ in range(N):
        score = list(map(int,input().split()))
        a.append(score)
    cnt=0
    a.sort()
    for i in range(1,N+1):
        if a[0][1]>=a[i][1]:
            cnt+=1
    a=[]
    print(cnt)
    

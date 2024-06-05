import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for i in range(1,N):
    A[i] = A[i] + A[i-1]

for i in range(Q):
    x,y = map(int,input().split())
    if x == 1:
        print(A[y-1])
    else:
        print(A[y-1] - A[x-2])
    
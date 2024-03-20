T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    B.sort()
    C = 0
    
    for i in range(n):
        l = 0
        r = m-1
        while l < r:
            mid = (l+r)//2
            if B[mid] <= A[i]:
                l = mid+1
            else:
                r = mid
        
        if l == 0:
            C += B[0]
        else:
            if A[i]-B[l-1] > B[l] - A[i]:
                C+=B[l]
            else:
                C+=B[l-1]
    print(C)
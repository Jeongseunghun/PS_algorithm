def solution(A, B):
    ans = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    aidx = 0
    bidx = 0
    
    for i in range(len(A)):
        if B[bidx] > A[aidx]:
            ans+=1
            aidx += 1
            bidx += 1
        else:
            aidx += 1
            
            
         
    return ans
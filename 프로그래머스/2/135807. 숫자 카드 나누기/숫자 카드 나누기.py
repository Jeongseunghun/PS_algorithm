import math

def solution(arrayA, arrayB):
    
    #가장 작은 수의 약수 찾는 함수
    def div(num):
        lst = set()
        lst.add(num)
        
        for i in range(1,int(math.sqrt(num)) + 1):
            if num % i == 0:
                lst.add(i)
                lst.add(num//i)
        
        return list(sorted(lst))
    
    def chk(lst,arrayA,arrayB):
        lst.sort(reverse = True)
        
        ans = 0
        for i in lst:
            flag = True
            for a,b in zip(arrayA,arrayB):
                if a % i != 0 or b % i == 0:
                    flag = False
                    break
            if flag:
                ans = max(ans,i)
            
        return ans
    
    A = div(min(arrayA))
    B = div(min(arrayB))
    
    ans = max(chk(A,arrayA,arrayB),chk(B,arrayB,arrayA))

    return ans
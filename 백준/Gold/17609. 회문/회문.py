T = int(input())

def chk2(pali,l,r):
    while l<r:
        if pali[l] == pali[r]:
            l+=1
            r-=1
        else:
            return False
    return True

def chk(pali,l,r):
    while l < r :
        #문자 같으면 다음으로 넘어감
        if pali[l] == pali[r]:
            l += 1
            r -= 1
        #문자 다르면
        else:
            l_remove = chk2(pali,l+1,r)
            r_remove = chk2(pali,l,r-1)
            if l_remove or r_remove:
                return 1
            else:
                return 2
    return 0
                
for i in range(T):
    pali = input()
    
    l = 0 
    r = len(pali) - 1
    print(chk(pali,l,r))
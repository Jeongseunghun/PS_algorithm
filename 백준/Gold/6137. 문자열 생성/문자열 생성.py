N = int(input())
S = [input() for _ in range(N)]

T = ''

l = 0
r = N-1

while l <= r:
    if S[l] < S[r]:
        T += S[l]
        l+=1
    elif S[l] > S[r]:
        T += S[r]
        r-=1
    #같으면
    else:
        l2,r2 = l+1, r-1
        flag = False
        while l2 <= r2:
            if S[l2] < S[r2]:
                T += S[l]
                l+=1
                flag = True
                break
            elif S[l2] > S[r2]:
                T += S[r]
                r-=1
                flag = True
                break
            l2+=1
            r2-=1
        if not flag:
            T += S[l]
            l += 1

for i in range(0,N,80):
    print(T[i:i+80],sep='\n')
    
                
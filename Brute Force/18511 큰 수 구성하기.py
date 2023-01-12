from itertools import product

N,K = map(int,input().split())
lst = list(map(str,input().split()))

digit = len(str(N))

while(True):
    temp = list(product(lst,repeat=digit))
    ans = []
    
    for i in temp:
        if int(''.join(i)) <= N:
            ans.append(int("".join(i)))
    
    if len(ans) >=1:
        print(max(ans))
        break
    else:
        digit -=1

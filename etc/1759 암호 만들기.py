L,C=map(int,input().split())
pw=list(map(str,input().split()))
pw.sort()

vowel = ['a','e','i','o','u']
ans = []

def chk(s):
    mo=0
    ja=0
    for i in range(L):
        if ans[i] in vowel:
            mo +=1
        else:
            ja+=1
    if mo>=1 and ja>=2:
        return True
    else:
        return False

def func():
    if len(ans) == L:
        if chk(ans):
            print(''.join(ans))
        return
    else:
        for i in pw:
            if not ans:
                ans.append(i)
                func()
                ans.pop()
            elif (i not in ans) and (i > ans[-1]):
                ans.append(i)
                func()
                ans.pop()
                
                
func()
    
            
        
    








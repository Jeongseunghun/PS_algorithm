L, C = map(int,input().split())
alpha = list(input().split())
alpha.sort()
vowels = ['a','e','i','o','u']
ans = []
def back(cnt,s):
    if cnt == L:
        c = 0
        v = 0
        for i in ans:
            if i in vowels:
                v += 1
            else:
                c += 1

        if c >= 2 and v >= 1:
            print(''.join(ans))

        return ans

    for i in range(s,C):
        ans.append(alpha[i])
        back(cnt+1,i+1)
        ans.pop()

back(0,0)

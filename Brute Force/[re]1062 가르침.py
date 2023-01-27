# 시간초과
# from itertools import combinations

# n,k = map(int,input().split())
# lst = []
# for i in range(n):
#     lst.append(input().strip('antatica'))

# cnt = 0 
# teachcnt = k-5

# if teachcnt < 0:
#     print(0)
#     exit()

# allcase = combinations(set(''.join(lst)),teachcnt)

# combi = []
# for i in allcase:
#     combi.append(''.join(i))

# ans = 0
# res = [[] for _ in range(len(lst))]
# for j in range(len(combi)):
#     for i in range(len(lst)):
#         res[i] = lst[i].strip(combi[j])
#     ans = max(ans,res.count(''))

# print(ans)


from itertools import combinations
n,k = map(int,input().split())

word = [0] * n
ans = 0
for i in range(n):
    temp = input()
    for x in temp:
        word[i] |= (1 << (ord(x) - ord('a')))

if k < 5:
    print(0)
else:
    alpha = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    need = ['a','c','t','i','n']
    for i in list(combinations(alpha,k-5)):
        each = 0
        res =0 
        for j in need:
            each |=(1 << (ord(j) - ord('a')))
        for j in i:
            each |=(1<< (ord(j) - ord('a')))
        
        for j in word:
            if each & j == j:
                res += 1
        
        if ans < res:
            ans = res
    
    print(ans)
            
            


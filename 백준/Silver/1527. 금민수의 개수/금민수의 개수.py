def dfs(i,str):
    global ans
    if i == len(str):
        if int(str) >= A and int(str) <= B:
            ans+=1
            return
        return
    for l in lst:
        dfs(i,str+l)

A,B = map(int,input().split())

lst = ['4','7']

#A의 자릿수
ad = len(str(A))
#B의 자릿수
bd = len(str(B))

ans = 0

for i in range(ad,bd+1):
    dfs(i,'')

        
print(ans)
    
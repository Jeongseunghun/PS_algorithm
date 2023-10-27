k = int(input())
s = list(map(str,input().split()))
visited = [0] * 10
ans = []

def chk(a,b,op):
    if op == '<':
        if a>b:
            return False
    if op == ">":
        if a<b:
            return False
    return True

def dfs(cnt,num):
    if cnt == k+1:
        ans.append(num)
        return
    
    for i in range(10):
        if visited[i]:
            continue
        if cnt == 0 or chk(num[cnt-1],str(i),s[cnt-1]):
            visited[i] = 1
            dfs(cnt+1,num+str(i))
            visited[i] = 0

dfs(0,'')

#크기순 정렬
ans.sort()
print(ans[-1])
print(ans[0])
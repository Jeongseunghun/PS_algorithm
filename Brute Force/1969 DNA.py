from re import L


N,M = map(int,input().split())
dna =[]
for _ in range(N):
    dna.append(list(input()))
    
ans = ""

for i in range(M):
    dic = {"A" : 0 , "C" : 0 , "G" : 0 , "T" : 0}
    for j in range(N):
            dic[dna[j][i]] +=1
    dic = sorted(dic,key = lambda x : dic[x],reverse=True)
    ans+=dic[0]
 
cnt = 0    
for i in range(N):
    for j in range(M):
        if ans[j] != dna[i][j]:
            cnt+=1
    
    
print(ans)
print(cnt)
           


n,d = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    for j in str(i):
        if j == str(d):
            cnt+=1

print(cnt)
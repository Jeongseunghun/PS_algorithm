N = int(input())
cnt = {}
a=0
for i in range(N):
    cow,loc = map(int,input().split())
    if cow not in cnt:
        cnt[cow] = loc
    else:     
        if cnt[cow] != loc:
            a+=1
            cnt[cow] = loc

print(cnt)


    
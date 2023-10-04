T = int(input())
word = list(input())

ans = 0
for _ in range(T-1):
    A = input()
    tmp = word[:]
    cnt = 0
    for i in A:
        if i in tmp:
            tmp.remove(i)
        else:
            cnt+=1
        
    if cnt <= 1 and len(tmp) <= 1:
        ans+=1

print(ans)
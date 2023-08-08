n = input()
duck = 'quack'
cnt = [0 for _ in range(len(n))]

ans = 0 
def check(i):
    global ans
    k = 0
    start = True
    for j in range(i,len(n)):
        if duck[k] == n[j] and not cnt[j]:
            cnt[j] = 1
            if n[j] == 'k':
                if start:
                    ans += 1
                    start = False
                k = 0
                continue
            k += 1


if len(n) % 5 !=0:
    print(-1)
    exit()
else:
    for i in range(len(n)):
        #q로 시작하고 방문하지 않았으면 체크 시작
        if n[i] == 'q' and not cnt[i]:
            check(i)

if not all(cnt) or ans == 0:
    print(-1)
else:
    print(ans)
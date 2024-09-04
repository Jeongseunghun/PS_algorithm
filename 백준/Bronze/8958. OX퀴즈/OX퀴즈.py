T = int(input())
for _ in range(T):
    s = input()
    ans = 0
    p = 0
    for i in s:
        if i == 'O':
            p += 1
        else:
            p = 0
        ans += p    
    print(ans)
        
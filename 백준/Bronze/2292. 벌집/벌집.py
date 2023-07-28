N = int(input())

ans = 1

cnt = 1
while N > ans:
    ans += 6*cnt
    cnt += 1

print(cnt)
    
    
    
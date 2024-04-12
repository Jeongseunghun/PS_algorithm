N = int(input())
ans = 0
x,y = map(int,input().split())
for _ in range(N-1):
    tx, ty = map(int, input().split())
    #포함하면
    if x <= ty <= y:
        continue
    #y가 범위 넘으면
    elif x<=tx<=y and not x<=ty<=y:
        y = ty
    #x부터 넘으면 새로 시작
    else:
        ans += y-x
        x,y = tx,ty

ans += y-x

print(ans)
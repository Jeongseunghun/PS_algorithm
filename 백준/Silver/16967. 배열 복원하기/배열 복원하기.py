H,W,X,Y = map(int,input().split())
b_arr = [list(map(int,input().split())) for _ in range(H+X)]

a_arr = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        a_arr[i][j] = b_arr[i][j]

for i in range(X,H):
    for j in range(Y,W):
        a_arr[i][j] = b_arr[i][j] - a_arr[i-X][j-Y]


for i in range(H):
    print(*a_arr[i])
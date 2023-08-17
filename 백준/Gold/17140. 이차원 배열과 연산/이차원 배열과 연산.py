r,c,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(3)]

def RC_sort(board,dir):
    tmp = [[] for _ in range(len(board))]
    length = 0
    for i in range(len(board)):
        val = set(board[i])
        for j in val:
            if j == 0:
                continue
            cnt = 0
            for k in board[i]:
                if j == k:
                    cnt+=1
            tmp[i].append((j,cnt))
        tmp[i] = sorted(tmp[i], key = lambda x: (x[1],x[0]))   
    
    ans = [[] for _ in range(len(tmp))]
    for i in range(len(tmp)):
        for j in tmp[i]:
            for k in j:
                ans[i].append(k)
    for i in ans:
        length = max(length, len(i))
    for i in ans:
        i += [0] * (length - len(i))
        if len(i) > 100:
            i = i[:100]
            
    return list(zip(*ans)) if dir == 'C' else ans

t = 0
while True:
    
    if 100 < t:
        t = -1
        break
    
    if 0 <= r-1 < len(board) and 0 <= c-1 < len(board[0]) and board[r-1][c-1] == k:
        break
    
    #행>=열
    if len(board) >= len(board[0]):
        board = RC_sort(board,'R')
    else:
        board = RC_sort(list(zip(*board)),'C')

    t+=1

print(t)
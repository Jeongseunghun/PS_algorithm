# from collections import deque

# R,C,N= map(int,input().split())

# board = [list(input()) for _ in range(R)]


# #상하좌우
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# q = deque()


# def bfs(q,board):
#     while q:
#         x,y = q.popleft()
#         board[x][y] = '.'
#         for i in range(4):
#             nx,ny = x+dx[i], y+dy[i]
#             if 0<= nx<R and 0 <= ny<C and board[nx][ny] == 'O':
#                 board[nx][ny] = '.'

# def simulate(t):
#     global q, board
#     if t == 1:
#         for i in range(R):
#             for j in range(C):
#                 if board[i][j] == 'O':
#                     q.append((i,j))
#     elif t%2 == 1:
#         bfs(q,board)
#         for i in range(R):
#             for j in range(C):
#                 if board[i][j] == 'O':
#                     q.append((i,j))
#     else:
#         board = [['O']*C for _ in range(R)]
    
    
# for i in range(1,N+1):
#     simulate(i)

# for i in board:
#     print(''.join(i))
                
                



from collections import deque           
            
R,C,N = map(int,input().split())

graph = [list(input()) for _ in range(R)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()


def bfs(q,graph):
    while q:
        x,y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx and nx<R and 0<= ny and ny < C and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'
            
            

def go(t):
    global q,graph
    if t == 1 :
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':
                    q.append((i,j))
    
    elif t % 2 == 1:
        bfs(q,graph)
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':
                    q.append((i,j))            
    
    else:
        graph = [['O']*C for _ in range(R)]


for i in range(1,N+1):
    go(i)

for i in graph:
    print(''.join(i))

        
        
            
            
        
        
        
        


         
        
        

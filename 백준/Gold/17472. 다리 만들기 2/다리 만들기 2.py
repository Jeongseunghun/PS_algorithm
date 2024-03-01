from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j, cnt):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    board[i][j] = cnt
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    board[nx][ny] = cnt
                    visited[nx][ny] = True
                    q.append((nx, ny))

def bridge(x, y, island):
    for k in range(4):
        cnt = 0
        nx, ny = x, y
        while True:
            nx += dx[k]
            ny += dy[k]
            cnt += 1
            if not (0 <= nx < N) or not (0 <= ny < M):
                break
            if board[nx][ny] == island:
                break
            if board[nx][ny] != 0:
                other_island = board[nx][ny]
                if cnt >= 3:  # 최소 길이는 3 이상이어야 함 (1과 0 사이의 길이)
                    lst.append((island, other_island, cnt - 1))
                break

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    A = find(a)
    B = find(b)
    if A == B:
        return False
    if A > B:
        parents[A] = B
    elif A < B:
        parents[B] = A
    return True

def kruskal(edges):
    edges.sort(key=lambda x: x[2])
    total_length = 0
    selected_edges = []
    for edge in edges:
        u, v, length = edge
        if find(u) != find(v):
            union(u, v)
            selected_edges.append(edge)
            total_length += length
    return selected_edges, total_length

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 2
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j, cnt)
            cnt += 1
            visited = [[False] * M for _ in range(N)]  # 섬을 번호 붙인 후에는 visited 배열 초기화

island_cnt = cnt - 2
lst = []
parents = [i for i in range(island_cnt + 2)]

for island in range(2, island_cnt + 2):
    for i in range(N):
        for j in range(M):
            if board[i][j] == island:
                bridge(i, j, island)

selected_bridges, total_length = kruskal(lst)

if len(selected_bridges) == island_cnt - 1:
    print(total_length)
else:
    print(-1)
def solution(n, computers):     
    def dfs(j):
        if lst[j] == 1:
            return
        lst[j] = 1
        for i in node[j]:
            dfs(i)
        return
    
    answer = 0
    N = len(computers)
    M = len(computers[0])
    lst = [0 for _ in range(n)]
    node = [[] for _ in range(n)]
    
    for i in range(N):
        for j in range(M):
            if computers[i][j] == 1:
                node[i].append(j)

    for i in node:
        for j in i:
            if lst[j] == 0:
                dfs(j)

                answer+=1

    return answer
score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,22,24,28,27,26,30,35,0]
#이동가능한 인덱스
graph = [[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,25],[12],[13],[14],[15],[16,27],[17],[18],[19],[20],[32],[22],[23],[24],[30],[26],[24],[28],[29],[24],[31],[20],[32]]

dice = list(map(int,input().split()))
ans = 0
def backtracking(loc,res,horse,test):
    global ans
    if loc > 10:
        ans = max(ans,res)
        return
    #말 네개 이동
    for i in range(4):
        #말 현재 위치
        x = horse[i]
        #이동할 수 있는 경우가 두개면 파란색 이동
        if len(graph[x]) == 2:
            x = graph[x][1]
        else:
            x = graph[x][0]
        for j in range(1,dice[loc-1]):
            x = graph[x][0]
        if x == 32 or (x<32 and x not in horse):
            before = horse[i]
            horse[i] = x
            test.append(x)
            backtracking(loc+1,res+score[x],horse,test)
            test.pop()
            horse[i] = before

backtracking(1,0,[0,0,0,0],[])
print(ans)
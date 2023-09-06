score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,22,24,28,27,26,30,35,0]
#이동가능한 인덱스 정보
graph = [[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,25],[12],[13],[14],[15],[16,27],[17],[18],[19],[20],[32],[22],[23],[24],[30],[26],[24],[28],[29],[24],[31],[20],[32]]

dice = list(map(int,input().split()))
ans = 0
def backtracking(depth,res,horse):
    global ans
    #10턴 지나면
    if depth == 10:
        ans = max(ans,res)
        return
    #말 네개 이동
    for i in range(4):
        #i번째 말 현재 위치
        x = horse[i]
        #이동할 수 있는 경우가 두 개면 파란색 루트 좌표
        if len(graph[x]) == 2:
            x = graph[x][1]
        #한 개면 빨간색 루트 좌표
        else:
            x = graph[x][0]
        #주사위 값만큼 이동
        for _ in range(1,dice[depth]):
            x = graph[x][0]
        #목적지 도착했거나 목적지에 도착하지 않았는데 말이 없다면
        if x == 32 or (x<32 and x not in horse):
            before = horse[i]
            horse[i] = x
            backtracking(depth+1,res+score[x],horse)
            horse[i] = before

backtracking(0,0,[0,0,0,0])
print(ans)
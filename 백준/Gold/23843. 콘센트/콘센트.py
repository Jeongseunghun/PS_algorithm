import heapq

N,M = map(int,input().split())
con = list(map(int,input().split()))
con.sort(reverse= True)

#현재 충전중인 전자기기 걸리는 시간 넣어주기
h = []

for i in con:
    #콘센트 비어있으면 채워 넣기
    if len(h) < M:
        heapq.heappush(h,i)
    else:
        tmp = heapq.heappop(h)
        heapq.heappush(h,tmp+i)

print(max(h))
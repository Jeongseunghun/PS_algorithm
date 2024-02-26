import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
INF = 1e9
#무한으로 초기화
dp = [INF] * (V+1)
h = []
graph = [[] for _ in range(V+1)]

def Dijkstra(s):
    #시작 정점은 0으로 초기화
    dp[s] = 0
    #가중치와 시작점
    heapq.heappush(h,(0,s))

    while h:
        weight,n = heapq.heappop(h)
        #가중치가 더 크면 무시
        if dp[n] < weight:
            continue

        for w,next_node in graph[n]:
            next_weight = w+weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                heapq.heappush(h,(next_weight,next_node))

for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])
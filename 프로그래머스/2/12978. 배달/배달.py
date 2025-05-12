import heapq

def solution(N, road, K):
    
    #최소 거리
    dist = [1e9 for _ in range(N+1)]
    dist[1] = 0
    nodes = [[] for _ in range(N+1)]
    for a,b,c in road:
        nodes[a].append((b,c))
        nodes[b].append((a,c))
        
    def dijkstra(dist,nodes):
        h = []
        heapq.heappush(h,[1,0])
        while h:
            node, cost = heapq.heappop(h)
            for n,c in nodes[node]:
                if cost + c < dist[n]:
                    dist[n] = cost + c
                    heapq.heappush(h,[n,cost+c])
    
    dijkstra(dist,nodes)
    
    return len([i for i in dist if i <= K])
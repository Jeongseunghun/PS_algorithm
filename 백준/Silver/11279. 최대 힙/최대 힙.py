import heapq,sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    a = int(input())
    if a > 0:
        heapq.heappush(heap,-a)
    elif a == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)

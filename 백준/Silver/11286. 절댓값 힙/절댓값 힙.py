import heapq,sys

input = sys.stdin.readline

N = int(input())
heap=[]
heapq.heapify(heap)
for i in range(N):
    tmp = int(input())
    if tmp != 0:
        heapq.heappush(heap,(abs(tmp),tmp))
    else:
        if heap:
            ans = heapq.heappop(heap)[1]
            print(ans)
        else:
            print(0)
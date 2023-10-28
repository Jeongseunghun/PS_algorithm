import heapq

N = int(input())
card = [int(input()) for _ in range(N)]
heapq.heapify(card)

tmp = 0
ans = 0
while len(card)>1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    tmp = a+b
    heapq.heappush(card,tmp)
    ans += a+b
print(ans)
#최대 가격부터 넣어주기
import heapq
import sys

input = sys.stdin.readline

N,K = map(int,input().split())
h = []

for _ in range(N):
    M,V = map(int,input().split())
    #무게, 가격
    heapq.heappush(h,(M,V))

#가방별 담을 수 있는 무게
bag = []
for _ in range(K):
    C = int(input())
    bag.append(C)

bag.sort()

ans = 0
lst = []
for i in bag:
    while h:
        m, v = heapq.heappop(h)
        if m <= i:
            heapq.heappush(lst,-v)
        else:
            heapq.heappush(h,(m,v))
            break

    if lst:
        ans += -heapq.heappop(lst)

print(ans)
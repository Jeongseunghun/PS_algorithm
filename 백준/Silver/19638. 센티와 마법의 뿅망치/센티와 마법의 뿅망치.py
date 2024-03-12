import heapq,sys

input = sys.stdin.readline

def chk():
    for i in giant:
        if H <= abs(i):
            return False
    return True

N,H,T = map(int,input().split())

giant = []
for i in range(N):
    g = int(input())
    heapq.heappush(giant,-g)

cnt = 0
flag = False
while True:
    flag = chk()
    if flag:
        print("YES")
        print(cnt)
        break
    cnt +=1
    tmp = -heapq.heappop(giant)
    tmp2 = tmp
    if tmp > 1:
        tmp //= 2
    heapq.heappush(giant,-tmp)
    if cnt > T:  
        print("NO")
        print(tmp2)
        break
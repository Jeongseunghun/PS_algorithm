import heapq,sys
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    k = int(input())
    max_h = []
    min_h = []
    chk = [0] * k
    
    for i in range(k):
        oper,n = input().split()
        #삽입
        if oper == 'I':
            heapq.heappush(min_h,(int(n),i))
            heapq.heappush(max_h,(-int(n),i))
            #두개 힙에 존재하면 1
            chk[i] = 1
        #최솟값 삭제
        elif oper == 'D' and n == "-1":
            while min_h and not chk[min_h[0][1]]:
                heapq.heappop(min_h)
            if min_h:
                chk[min_h[0][1]] = 0
                heapq.heappop(min_h)
        #최댓값 삭제   
        elif oper == 'D' and n == "1":
            while max_h and not chk[max_h[0][1]]:
                heapq.heappop(max_h)
            if max_h:
                chk[max_h[0][1]] = 0
                heapq.heappop(max_h)
    
    while min_h and not chk[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not chk[max_h[0][1]]:
        heapq.heappop(max_h)

    if len(max_h) == 0 and len(min_h) == 0:
        print("EMPTY")
    else:
        print(-max_h[0][0],min_h[0][0])
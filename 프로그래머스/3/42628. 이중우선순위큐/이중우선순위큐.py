import heapq

def solution(operations):
    max_h = []
    min_h = []
    flag = [0 for _ in range(len(operations))]
    
    for idx,i in enumerate(operations):
        command,val = i.split(" ")
        #삽입
        if command == 'I':
            heapq.heappush(max_h,(-int(val),idx))
            heapq.heappush(min_h,(int(val),idx))
            flag[idx] = 1
        #최댓값 삭제
        elif command == 'D' and val == '1':
            while max_h and not flag[max_h[0][1]]:
                heapq.heappop(max_h)
            if max_h:
                flag[max_h[0][1]] = 0
                heapq.heappop(max_h)
                
        #최솟값 삭제
        elif command == 'D' and val == '-1':
            while min_h and not flag[min_h[0][1]]:
                heapq.heappop(min_h)
            if min_h:
                flag[min_h[0][1]] = 0
                heapq.heappop(min_h)
    
    while max_h and not flag[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not flag[min_h[0][1]]:
        heapq.heappop(min_h)
    
    if len(max_h) == 0 and len(min_h) == 0:
        return [0,0]

    return [-max_h[0][0],min_h[0][0]]

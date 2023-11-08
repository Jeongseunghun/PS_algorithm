import heapq,sys
input = sys.stdin.readline

N = int(input())
max_lst = []
min_lst = []

for i in range(N):
    num = int(input())
    if len(max_lst) == len(min_lst):
        heapq.heappush(max_lst,-num)
    else:
        heapq.heappush(min_lst,num)
    
    if min_lst and min_lst[0] < -max_lst[0]:
        max_val = heapq.heappop(max_lst)
        min_val = heapq.heappop(min_lst)
        
        heapq.heappush(max_lst,-min_val)
        heapq.heappush(min_lst,-max_val)
    
    print(-max_lst[0])
    
    
import heapq

def chk(lst):
    l,r = [],[]
    m = lst[0]
    res = [m]
    for i,v in enumerate(lst[1:],1):
        if v > m:
            heapq.heappush(r,v)
        else:
            heapq.heappush(l,-v)
        if i % 2 == 0:
            if len(l) < len(r):
                heapq.heappush(l,-m)
                m = heapq.heappop(r)
            elif len(l) > len(r):
                heapq.heappush(r,m)
                m = -heapq.heappop(l)
            res.append(m)

    print(len(res))

    for i in range(len(res)):
        if (i+1) != 1 and (i+1) % 10 == 1:
            print()
        print(res[i], end = ' ')
    print()



T = int(input())
for _ in range(T):
    M = int(input())
    lst = []
    if M <= 10:
        lst = list(map(int,input().split()))
    else:
        lst = []
        for i in range(M//10+1):
            tmp_lst = list(map(int,input().split()))
            for j in tmp_lst:
                lst.append(j)

    chk(lst)
N = int(input())
start = list(map(int,input()))
end = list(map(int,input()))

def switch(start,end):
    copy=start[:]
    cnt=0
    for i in range(1,N):
        if copy[i-1] == end[i-1]:
            continue
        
        cnt+=1
        for j in range(i-1,i+2):
            if j<N:
                copy[j] = 1-copy[j]
    if copy == end:
        return cnt
    else:
        return 1e9

res = switch(start,end)

start[0] = 1 - start[0]
start[1] = 1 - start[1]
res = min(res, switch(start,end) + 1)
print(res if res!= 1e9 else -1)
    
        
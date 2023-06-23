T = int(input())
for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx,cy,r=map(int,input().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        length = r ** 2
        
        if length > dis1 and length > dis2:
            pass
        elif length > dis1:
            cnt+=1
        elif length > dis2:
            cnt+=1
        
    print(cnt)
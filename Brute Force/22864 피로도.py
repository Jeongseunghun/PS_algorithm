A,B,C,M = map(int,input().split())

res = 0
sta = 0


for i in range(24):
    if sta+A <= M:
        res += B
        sta += A
        
    elif sta+A > M:
        sta -= C
        if sta < 0:
            sta = 0        
print(res)
        
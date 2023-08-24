N = int(input())
city = [list(map(int,input().split())) for _ in range(N)]

s = 0
for i in city:
    s += sum(i)
    
def div(x,y,d1,d2):
    global ans,s
    one,two,three,four = 0,0,0,0
    
    #1구역
    y1 = y + 1
    for i in range(x+d1):
        if i >= x:
            y1 -= 1
        one += sum(city[i][:y1])
    
    #2구역
    y2 = y + 1
    for i in range(x+d2+1):
        if i > x:
            y2 += 1
        two += sum(city[i][y2:])
    
    #3구역
    y3 = y - d1
    for i in range(x+d1, N):
        three += sum(city[i][:y3])
        if i < x+d1+d2:
            y3 += 1
    
    #4구역
    y4 = (y+d2) - N
    for i in range(x+d2+1,N):
        four += sum(city[i][y4:])
        if i <= x+d1+d2:
            y4 -= 1
    
    #5구역
    five = s - (one+two+three+four)
    
    ans = min(ans,(max(one,two,three,four,five) - min(one,two,three,four,five)))

ans = 1e9

#모든 선거구 나누는 방법 구하기
for x in range(N-2):
    for y in range(1,N-1):
        for d1 in range(1,N-1):
            for d2 in range(1,N-1):
                if 0 <= x + d2 < N and 0 <= y+d2 < N and x+d1+d2 < N and y-d1+d2 < N and x+d1>0 and y-d1>0:
                        div(x,y,d1,d2)
                    
print(ans)
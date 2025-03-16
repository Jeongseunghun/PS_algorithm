def solution(dirs):
    answer = 0
    
    sx,sy = 0,0
    ex,ey = 0,0
    
    dir = {'U':(0,-1), 'D':(0,1), 'R':(1,0), 'L':(-1,0)}
    
    #갔던 길
    dict = []
       
    for d in dirs:
        x,y = dir[d]
        if ex + x > 5 or ey + y > 5 or ex + x < -5 or ey + y < -5:
            continue
        if (ex, ey, ex + x, ey + y) not in dict and (ex+x,ey+y,ex,ey) not in dict:
            sx = ex
            sy = ey
            ex = sx + x
            ey = sy + y
            dict.append((sx, sy, ex, ey))
        else:
            sx = ex
            sy = ey
            ex = sx + x
            ey = sy + y

        
    
    return len(dict)
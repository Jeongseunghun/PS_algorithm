import rlcompleter


l,r = input().split()
m = list(input())



pad = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]

#초기 위치
for i in range(3):
    for j in range(len(pad[i])):
        if pad[i][j] == l:
            lx = i
            ly = j
        if pad[i][j] == r:
            rx = i
            ry = j
            
#주어진 값 위치
m_loc=[]
for k in range(len(m)):
    for i in range(3):
        for j in range(len(pad[i])):
            if pad[i][j] == m[k]:
                m_loc.append([i,j])
        

#거리비교
val=[1] * len(m)
for i in range(len(m)):
    val[i] += min(abs(m_loc[i][0]-lx)+abs(m_loc[i][1]-ly),abs(m_loc[i][0]-rx)+abs(m_loc[i][1]-ry))
    # if val[i] == abs(m_loc[i][0]-lx)+abs(m_loc[i][1]-ly):
    #     lx = m_loc[i][0]
    #     ly = m_loc[i][1]
    # elif val[i] == abs(m_loc[i][0]-rx)+abs(m_loc[i][1]-ry):
    #     rx = m_loc[i][0]
    #     ry = m_loc[i][1]
        

print(val)
            
        
        
    

import rlcompleter


l,r = input().split()
m = list(input())



padl = [['q','w','e','r','t'],['a','s','d','f','g'],['z','x','c','v','b']]
padr = [['','y','u','i','o','p'],['','h','j','k','l'],['b','n','m']]

#초기 위치
for i in range(3):
    for j in range(len(padl[i])):
        if padl[i][j] == l:
            lx = i
            ly = j

for i in range(3):
    for j in range(len(padr[i])):
        if padr[i][j] == r:
            rx = i
            ry = j


#주어진 값 위치
m_loc=[]


for k in range(len(m)):
    for l in range(3):
        if m[k] in padl[l]:
            for i in range(3):
                for j in range(len(padl)):
                    if padl[i][j] == m[k]:
                        m_loc.append([i,j])
        if m[k] in padr[l]:
            for i in range(3):
                for j in range(len(padr)):
                    if padr[i][j] == m[k]:
                        m_loc.append([i,j])
                    
        

# #거리비교
# val=[1] * len(m)
# for i in range(len(m)):
#     val[i] += min(abs(m_loc[i][0]-lx)+abs(m_loc[i][1]-ly),abs(m_loc[i][0]-rx)+abs(m_loc[i][1]-ry))
    # if val[i] == abs(m_loc[i][0]-lx)+abs(m_loc[i][1]-ly):
    #     lx = m_loc[i][0]
    #     ly = m_loc[i][1]
    # elif val[i] == abs(m_loc[i][0]-rx)+abs(m_loc[i][1]-ry):
    #     rx = m_loc[i][0]
    #     ry = m_loc[i][1]
        

print(m_loc)
            
        
        
    

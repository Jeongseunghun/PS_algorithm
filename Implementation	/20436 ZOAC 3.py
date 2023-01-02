import rlcompleter


l,r = input().split()
m = list(input())



padl = [['q','w','e','r','t'],['a','s','d','f','g'],['z','x','c','v']]
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
l_loc=[]
r_loc=[]


for k in range(len(m)):
    for l in range(3):
        if m[k] in padl[l]:
            for i in range(3):
                for j in range(len(padl[i])):
                    if padl[i][j] == m[k]:
                        l_loc.append([i,j])
    for l in range(3):
        if m[k] in padr[l]:
            for i in range(3):
                for j in range(len(padr[i])):
                    if padr[i][j] == m[k]:
                        r_loc.append([i,j])
                        

# print(l_loc, r_loc)

#거리비교
val = []

for i in range(len(l_loc)):
    val.append(abs(l_loc[i][0]-lx)+abs(l_loc[i][1]-ly))
    lx = l_loc[i][0]
    ly = l_loc[i][1]


for i in range(len(r_loc)):
    val.append(abs(r_loc[i][0]-rx)+abs(r_loc[i][1]-ry))
    rx = r_loc[i][0]
    ry = r_loc[i][1]
        

# print(val_l,val_r)
print(len(val) + sum(val))
            
        
        
    

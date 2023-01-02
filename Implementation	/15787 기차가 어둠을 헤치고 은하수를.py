N,M = map(int,input().split())
ktx=[[0] * 22 for _ in range(N)]


for j in range(M):
    command = list(map(int,input().split()))

    if command[0] == 1:
        ktx[command[1]-1][command[2]] = 1
    elif command[0] == 2:
        ktx[command[1]-1][command[2]] = 0
    elif command[0] == 3:
        for k in range(21,0,-1):
            ktx[command[1]-1][k] = ktx[command[1]-1][k-1]
        ktx[command[1]-1][-1] = 0
    elif command[0] == 4:
        for k in range(1,22):     
            ktx[command[1]-1][k-1] = ktx[command[1]-1][k] 
        ktx[command[1]-1][0] = 0
 

same = []
for i in range(N):
    if ktx[i] not in same:
        same.append(ktx[i])

print(len(same))
        
    
    
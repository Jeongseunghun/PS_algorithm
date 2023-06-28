N,L = map(int,input().split())
street = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

def check(line):
    for i in range(1,N):
        #1보다 크면 패스
        if abs(line[i] - line[i-1]) > 1:
            return False
        #앞이 클때
        if line[i] < line[i-1]:
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or slope[i+j]:
                    return False
                if line[i] == line[i+j]:
                    slope[i+j] = True
        #뒤가 클때
        elif line[i] > line[i-1]:
            for j in range(L):
                if i-j-1<0 or line[i-1] != line[i-j-1] or slope[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    slope[i-j-1] = True
    return True
                

for i in range(N):
    slope = [False] * N
    if check([street[i][j] for j in range(N)]):
        cnt += 1

for j in range(N):
    slope = [False] * N
    if check([street[i][j] for i in range(N)]):
        cnt += 1

print(cnt)
        
        
    
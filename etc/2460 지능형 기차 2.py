current = []
cnt = 0
for i in range(10):
    o,i = map(int,input().split())
    cnt += i
    cnt -= o
    current.append(cnt)

print(max(current))
    
    
    
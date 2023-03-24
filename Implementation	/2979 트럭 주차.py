A,B,C = map(int,input().split())

parking = [0] * 100

for _ in range(3):
    d,a = map(int,input().split())
    for i in range(d,a):
        parking[i] += 1
        
    

ans = 0

for i in parking:
    if i == 1:
        ans += A
    elif i == 2:
        ans += B*2
    elif i == 3:
        ans += C*3
    
    
print(ans)
    

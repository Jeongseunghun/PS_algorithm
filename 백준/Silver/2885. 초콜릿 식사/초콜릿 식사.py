K = int(input())

n = 0
for i in range(1,21):
    if 2**(i-1) < K <= 2**i:
        n = 2**i
        break

cnt = 0
s = n
while s:
    if K % s == 0:
        break
    s //= 2
    cnt += 1

print(n,cnt)
     
        
        
        
        
        
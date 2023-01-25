N=list(map(int,input()))
left = 0
right = 0

for i in range(int(len(N)/2)):
    left += N[i]
    right += N[-i-1]
    
if left == right:
    print('LUCKY')
else:
    print('READY')

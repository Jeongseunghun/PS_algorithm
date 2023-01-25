N=int(input())
rope=[]
res=[]

for i in range(N):
    rope.append(int(input()))
    
rope.sort(reverse=True)

for i in range(N):
    res.append(rope[i]*(i+1))

print(max(res))


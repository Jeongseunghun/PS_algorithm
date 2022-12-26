import sys
read = sys.stdin.readline

N,K = map(int,read().split())
thing = [0] * (K+1)

for _ in range(N):
    W,V = map(int,read().split())
    for j in range(K, W-1, -1):
        thing[j] = max(thing[j],thing[j-W]+V)
        
    
print(thing[-1])
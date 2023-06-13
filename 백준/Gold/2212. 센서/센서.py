N = int(input())
K = int(input())
m = list(map(int,input().split()))
m.sort()

dist = []
for i in range(1,N):
    dist.append(m[i] - m[i-1])

dist.sort(reverse=True)


print(sum(dist[K-1:]))
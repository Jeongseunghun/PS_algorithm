N=int(input())
seat = [[] for _ in range(N**2)]

for _ in range(N**2):
    num,a,b,c,d = list(map(int, input().split()))
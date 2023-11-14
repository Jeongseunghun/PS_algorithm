N,M = map(int,input().split())
dict = {}
for i in range(N):
    address,password = map(str,input().split())
    dict[address] = password

for i in range(M):
    ans = input()
    print(dict[ans])
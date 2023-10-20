N,M = map(int,input().split())
lst = {}


for i in range(N):
    word = input()
    if len(word) >= M:
        if word in lst:
            lst[word] += 1
        else:
            lst[word] = 1

lst = sorted(lst.items(), key = lambda x: (-x[1],-len(x[0]),x[0]))

for i in lst:
    print(i[0])
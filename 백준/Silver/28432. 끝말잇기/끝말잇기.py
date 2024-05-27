N = int(input())
lst = [input() for _ in range(N)]
M = int(input())
words = [input() for _ in range(M)]

ans = []

if N == 1:
    print(words[0])
else:
    for i in range(N):
        front = ''
        rear = ''
        if lst[i] == '?':
            if i == 0:
                rear = lst[i+1][0]
                for j in words:
                    if j[-1] == rear:
                        ans.append(j)
            elif i == N-1:
                front = lst[i-1][-1]
                for j in words:
                    if j[0] == front:
                        ans.append(j)
            else:    
                front = lst[i-1][-1]
                rear = lst[i+1][0]
                for j in words:
                    if j[0] == front and j[-1] == rear:
                        ans.append(j)

for i in ans:
    if i not in lst:
        print(i)
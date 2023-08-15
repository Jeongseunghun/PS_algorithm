N = int(input())
ans = []

for i in range(N):
    word = sorted(list(input()))
    if word not in ans:
        ans.append(word)
        
print(len(ans))

N = int(input())
build = []
for i in range(N):
    build.append(int(input()))

ans = 0
stack = []

for i in build:
    while stack and stack[-1]<=i:
        stack.pop()
    stack.append(i)
    
    ans += len(stack)-1

print(ans)
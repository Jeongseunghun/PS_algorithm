N = int(input())
lst = list(map(int,input().split()))

ans = [-1] * N
stack = []
for i in range(N):
    #스택 비어있지 않고 리스트의 스택 맨위 인덱스 값이 현재 값보다 작으면
    while stack and (lst[stack[-1]] < lst[i]):
        idx = stack.pop()
        ans[idx] = lst[i]
    stack.append(i)

print(*ans)
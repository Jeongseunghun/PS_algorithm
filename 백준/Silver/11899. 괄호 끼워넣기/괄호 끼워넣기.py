S = list(input())

stack = []
ans = 0
for i in range(len(S)):
    if S[i] == "(":
        stack.append(i)
    elif S[i] == ")":
        if stack:
            stack.pop()
        else:
            ans += 1
print(ans + len(stack))
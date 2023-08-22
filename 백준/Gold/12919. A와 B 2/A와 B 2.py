S = input()
T = input()

ans = 0
def dfs(t):
    global ans
    #바꿀 수 있으면
    if t == S:
        ans = 1
        return
    #바꿀 수 없으면
    if len(t) < 1:
        return
    #마지막이 A
    if t[-1] == "A":
        dfs(t[:-1])
    #처음이 B
    if t[0] == "B":
        dfs(t[::-1][:-1])

dfs(T)
print(ans)
    
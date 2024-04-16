T = int(input())
for _ in range(T):
    n = int(input())
    dict = {}
    one = list(input().split())
    for i in range(n):
        dict[one[i]] = i

    seq = {}
    two = list(input().split())
    for i in range(n):
        seq[i] = dict[two[i]]
    pwd = list(input().split())

    ans = [None] * n

    for i in range(n):
        ans[seq[i]] = pwd[i]

    print(*ans)
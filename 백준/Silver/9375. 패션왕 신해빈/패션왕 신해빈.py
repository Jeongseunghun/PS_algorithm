t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    num = 1
    for i in range(n):
        name,cat = input().split()
        if cat not in dict:
            dict[cat] = 1
        else:
            dict[cat] += 1
    for i in dict:
        num *= (dict[i]+1)
    print(num-1)
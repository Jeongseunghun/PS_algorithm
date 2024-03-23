cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    lst = [input() for _ in range(N)]
    print(cnt)
    lst.sort()
    for i in lst:
        print(i)
    cnt+=1
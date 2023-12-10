a,b = map(int,input().split())
a_lst = set(map(int,input().split()))
b_lst = set(map(int,input().split()))

ans = a_lst - b_lst

if ans == 0:
    print(0)
else:
    print(len(ans))
    print(*sorted(ans))
        
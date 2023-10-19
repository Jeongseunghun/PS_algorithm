N,game = map(str,input().split())
N = int(N)

lst = [input() for _ in range(N)]
lst = list(set(lst))

if game == 'Y':
    print(len(lst))
elif game == 'F':
    print(len(lst) // 2)
else:
    print(len(lst) // 3)
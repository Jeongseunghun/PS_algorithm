N = int(input())
name = [input() for _ in range(N)]

name_d = sorted(name,reverse=True)
name_i = sorted(name)

if name == name_i:
    print('INCREASING')
elif name == name_d:
    print('DECREASING')
else:
    print('NEITHER')
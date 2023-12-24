N = int(input())
lst = list(input().split())

tmp = {}
for i in lst:
    if i[-6:] == 'Cheese':
        if i in tmp:
            tmp[i]+=1
        else:
            tmp[i] = 1

if len(tmp) >= 4:
    print('yummy')
else:
    print('sad')
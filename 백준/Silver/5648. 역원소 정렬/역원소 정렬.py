lst = list(input().split())

n = int(lst[0])
lst.pop(0)

while True:
    tmp = list(input().split())
    lst+=tmp
    if len(lst) == n:
        break

a = []

for i in lst:
    a.append(int(i[::-1]))

a.sort()
for i in a:
    print(i)
    

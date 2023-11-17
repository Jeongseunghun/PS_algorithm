N = int(input())
lst = []
for i in range(N):
    num = int(input())
    lst.append(num)

lst.sort(reverse= True)

for i in lst:
    print(i)
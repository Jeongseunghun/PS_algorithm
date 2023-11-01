N = int(input())

lst = []
dict = {}
numlst = []

for i in range(N):
    a = input()
    lst.append(a)

for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j] in dict:
            dict[lst[i][j]] += 10**(len(lst[i])-j-1)
        else:
            dict[lst[i][j]] = 10**(len(lst[i])-j-1)

for i in dict.values():
    numlst.append(i)

numlst.sort(reverse=True)

sum = 0
pow = 9
for i in numlst:
    sum+= pow * i
    pow -= 1
    
print(sum)
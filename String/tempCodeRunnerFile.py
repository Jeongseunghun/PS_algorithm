N = int(input())
a = dict()
for i in range(N):
    name = input()
    if name[0] not in a:
        a[name[0]] =1
    else:
        a[name[0]] +=1
    
for k in a:
    if a[k] >= 5:
        print(k,end = "")

if max(a.values()) < 5:
    print("PREDAJA")

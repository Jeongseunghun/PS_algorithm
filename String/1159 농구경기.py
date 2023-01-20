# N = int(input())
# a = []
# for i in range(N):
#     name = input()
#     if name[0] not in a:
#         a[name[0]] =1
#     else:
#         a[name[0]] +=1
    
# for k in a:
#     if a[k] >= 5:
#         print(k,end = "")

# if max(a.values()) < 5:
#     print("PREDAJA")
    

a = sorted([input()[0] for _ in range(int(input()))])
lst = set(a)
res = []
for i in lst:
    if a.count(i) >= 5:
        res.append(i)

print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")

N = int(input())
dict = {}
for i in range(N):
    s = input()
    if s not in dict:
        dict[s] = 1
    else:
        dict[s] +=1

lst = []
dict = sorted(dict.items(),key = lambda x : -x[1])

m = max(dict)
print(* m)
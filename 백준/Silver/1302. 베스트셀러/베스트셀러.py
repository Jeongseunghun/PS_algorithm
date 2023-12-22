N = int(input())
dict = {}
for _ in range(N):
    book = input()
    if book not in dict:
        dict[book] = 1
    else:
        dict[book] +=1

dict = sorted(dict,key = lambda x : (-dict[x],x))

print(dict[0])
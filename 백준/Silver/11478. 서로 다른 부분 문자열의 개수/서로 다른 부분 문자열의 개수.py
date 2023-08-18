S = input()

lst = []
for i in range(len(S)):
    for j in range(len(S)):
        lst.append(S[i:i+j+1])
        
print(len(set(lst)))
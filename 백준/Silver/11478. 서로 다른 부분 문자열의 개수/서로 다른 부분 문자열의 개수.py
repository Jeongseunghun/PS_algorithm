S = input()

lst = []
for i in range(len(S)):
    for j in range(1,len(S)+1):
        lst.append(S[i:i+j])
        
print(len(set(lst)))

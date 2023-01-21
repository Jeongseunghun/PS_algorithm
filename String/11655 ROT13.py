S = input()
res =''

for i in S:
    if i.islower(): 
        res += chr(97 + (ord(i) + 13 - 97)%26)
    elif i.isupper():
        res += chr(65 + (ord(i) + 13 - 65)%26)
    else:
        res += i

print(res)
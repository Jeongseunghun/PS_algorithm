N = int(input())
dict = {}
cnt = 0
for i in range(N):
    word = input()
    if word == 'ENTER':
        cnt+=len(dict)
        dict = {}
    else:
        if word in dict:
            dict[word] +=1
        else:
            dict[word] = 1

print(len(dict)+cnt)

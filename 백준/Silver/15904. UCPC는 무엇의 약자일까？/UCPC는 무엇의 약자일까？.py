n = input()

ucpc = ['U','C','P','C']
flag = True

for i in range(4):
    if ucpc[i] in n:
        idx = n.find(ucpc[i])
        n = n[idx+1::]
    else:
        flag = False
        break

if flag == True:
    print('I love UCPC')
else:
    print('I hate UCPC')   
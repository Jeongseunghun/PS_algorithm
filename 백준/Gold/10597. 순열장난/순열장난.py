kriii = input()

lst = []

if len(kriii) < 10:
    n = len(kriii)
else:
    n = 9 + (len(kriii) - 9) // 2

def back(i):
    if i == len(kriii):
        print(*lst)
        exit()
    if kriii[i] != '0':
        one = kriii[i]
        two = kriii[i:i+2]
        if int(one) <= n and one not in lst:
            lst.append(one)
            back(i+1)
            lst.pop()
        if int(two) <= n and two not in lst:
            lst.append(two)
            back(i+2)
            lst.pop()

back(0)
    
    

    
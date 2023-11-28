N = int(input())
str = list(input())
num = [int(input()) for _ in range(N)]
lst = []
for i in str:
    if i.isalpha():
        lst.append(num[ord(i)-65])
    else:
        a = lst.pop()
        res = lst.pop()
        
        if i == '+':
            res += a
        elif i == '-':
            res -= a
        elif i == '*':
            res *= a
        elif i == '/':
            res /= a
        lst.append(res)

print('%.2f' %lst[-1])

lst = list(input())
digit = []

for i in lst:
    if i.isdigit():
        digit.append(int(i))
    else:
        x = digit.pop()
        y = digit.pop()
        if i == "+":
            tmp = x + y
            digit.append(tmp)
        elif i == "*":
            tmp = x * y
            digit.append(tmp)
        elif i == "/":
            tmp = y // x
            digit.append(tmp)
        elif i == "-":
            tmp = y - x
            digit.append(tmp)

print(digit[0])
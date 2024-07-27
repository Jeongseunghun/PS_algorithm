# H -> 1, C -> 12, O -> 16
def change(s):
    if s == 'H':
        return 1
    elif s == 'C':
        return 12
    elif s == 'O':
        return 16

chemi = input()

ans = 0
stack = []
    
for i in chemi:
    if i == '(':
        stack.append(i)
    elif i.isalpha():
        stack.append(change(i))
    elif i == ')':
        tmp = 0
        while True:
            if stack[-1] == '(':
                stack.pop()
                stack.append(tmp)
                break
            else:
                tmp += stack.pop()
    else:
        stack.append(stack.pop() * int(i))

print(sum(stack))

        
        
        

lst = list(input())

stack = []
cnt = 0


for i in range(len(lst)):
    if lst[i] == '(': 
        stack.append(lst[i])  
    elif lst[i] == ')':
        #레이저
        if stack and lst[i-1] == '(':
            stack.pop()
            cnt+=stack.count('(')
        elif stack:
            stack.pop(0)
            cnt+=1
        
print(cnt)
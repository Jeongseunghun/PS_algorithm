n = input()
explode = input()
stack = []

for i in range(len(n)):
    stack.append(n[i])
    if ''.join(stack[-len(explode):]) == explode:
        for i in range(len(explode)):
            stack.pop()
        
        
        
if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))


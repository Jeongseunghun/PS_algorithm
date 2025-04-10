s = input()

stack = []
for i in range(len(s)):
    if s[i] == "P":
        stack.append(s[i])
    elif s[i] == "A":
        if i == len(s)-1 or s[i+1] == "A":
            print("NP")
            exit()
        if len(stack) >= 2:
            if stack[-1] == "P" and stack[-2] == "P":
                stack.pop()
                stack.pop()
            else:
                stack.append(s[i])
        else:
            print("NP")
            exit()

if ''.join(stack) == 'P':
    print("PPAP")
else:
    print("NP")
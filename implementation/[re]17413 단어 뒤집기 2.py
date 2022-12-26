S = input()
stack = ""
res = ""

for i in S:
    if i == " ":
        if "<" not in stack:
            res += stack[::-1] + i
        else:
            stack += i
    elif i == "<":
        res += stack[::-1]
        stack = ''
        stack += i
        
    elif i == ">":
        res += stack + i
        stack = ''
    
    else:
        stack += i


res += stack[::-1]

    

    




        
        


print(res)
    
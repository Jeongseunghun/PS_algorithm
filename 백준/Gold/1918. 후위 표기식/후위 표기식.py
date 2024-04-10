st = list(input())

s = []

ans = ''        

#괄호 먼저 처리
for i in st:
    #문자면
    if i.isalpha():
        ans+=i
    else:      
        if i == "(":
            s.append(i)             
        #*,/연산자면
        elif i == "*" or i == "/":
            while s and (s[-1] =='*' or s[-1] == "/"):
                ans += s.pop()
            s.append(i)
        #+,-연산자면
        elif i == "+" or i == "-":
            while s and s[-1] !='(':
                ans += s.pop()
            s.append(i)
        elif i == ")":
            while s and s[-1] !='(':
                ans += s.pop()
            s.pop()       

while s:
    ans += s.pop()

print(ans)
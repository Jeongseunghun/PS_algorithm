s= list(input())
tag = False
res = ""
ans = ""

for i in s:
    # 거꾸로
    if tag == False:
        if i == "<":
            res+=i
            tag = True
        elif i == " ":
            res+=i
            ans+=res
            res=""
        else:
            res = i + res
     
    # 제대로       
    elif tag == True:
        if i == ">":
            res+=i
            tag = False
            ans+=res
            res=""
        else:
            res+=i
        
        
        
print(ans+res)
            
     

    
        
                        
        

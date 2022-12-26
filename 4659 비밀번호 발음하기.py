vowel = 'aeiou'

while True:
    s = input()
    if s == "end":
        break
    v=0
    k=1
    for i in range(len(s)):
        if s[i] in vowel:
           v = 1 
        if i > 0:
            if s[i]==s[i-1] and s[i] != 'e' and s[i] != 'o':
                k=0
                break
        if i > 1:
            if s[i] not in vowel:
                if s[i-1] not in vowel:
                    if s[i-2] not in vowel:
                        k=0
                        break
            if s[i] in vowel:
                if s[i-1] in vowel:
                    if s[i-2] in vowel:
                        k=0
                        break
    if v==1 and k==1:
        print("<" + s + "> is acceptable.")
    else:
        print("<" + s + "> is not acceptable.")

    
                
                
                
        
    


    
        
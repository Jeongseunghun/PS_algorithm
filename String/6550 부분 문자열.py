while True:
    try:
        s,t = input().split()
        idx = 0
        flag = 0
        for i in range(len(t)):
            if s[idx] == t[i]:
                idx+=1
                if len(s) == idx:
                    flag = 1
                    break
        
        if flag == 1:
            print("Yes")
        else:
            print("No")
        
        
    except:
        break

            

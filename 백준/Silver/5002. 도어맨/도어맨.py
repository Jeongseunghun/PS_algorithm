X = int(input())
lst = list(input())

stack = [lst[0]]
cnt = 1
for i in range(1,len(lst)-1):
    #현재 들어간 사람 성별 세기
    m = stack.count("M")
    w = stack.count("W")
    if abs(m-w) > X:
        print(cnt-1)
        exit(0)
    else:
        cnt+=1
        first_m = m
        first_w = w
        if lst[i] == 'M':
            first_m += 1
        elif lst[i] == 'W':
            first_w += 1
        
        second_m = m
        second_w = w
        if lst[i+1] == 'M':
            second_m += 1
        elif lst[i+1] == 'W':
            second_w += 1
        
        if abs(first_m - first_w) <= abs(second_m - second_w):
            stack.append(lst[i])
        else:
            tmp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = tmp
            stack.append(lst[i])


if abs(stack.count('M') - stack.count('W')) > X:
    print(cnt-1)
else:
    if lst[-1] == 'M':
        if abs((stack.count('M')+1) - stack.count('W')) > X:
            print(cnt)
            exit(0)
    elif lst[-1] == 'W':
        if abs((stack.count('M')) - (stack.count('W')+1)) > X:
            print(cnt)
            exit(0)
    cnt+=1
    print(cnt)
        
        
            
        
    


def new_sum(num:int):
    new_total = 0
    while num:
        if(num % 10) % 2 == 1:
            new_total += 1
        num//=10
    return new_total

def sol(n:str, total:int):  #현재 수, 현재까지 홀수 개수
    if len(n) == 1:
        case.append(total)
        return
    elif len(n) == 2:
        new_num = int(n[0]) + int(n[1])
        sol(str(new_num), total+new_sum(new_num))
    else:
        for i in range(1,len(n)):
            for j in  range(i+1, len(n)):
                part1 = n[:i]
                part2 = n[i:j]
                part3 = n[j:]
                
                new_num = int(part1) + int(part2) + int(part3)
                sol(str(new_num), total+new_sum(new_num))
            



N= input()
case = []
sol(N, new_sum(int(N)))
print(min(case),max(case))





    

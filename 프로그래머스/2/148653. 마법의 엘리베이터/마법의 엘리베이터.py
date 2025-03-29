def solution(storey):
    answer = 0
    
    while storey:
        
        n = storey % 10
        #5보다 클 때
        if n > 5:
            answer += 10-n
            storey += 10
        #5보다 작을 때
        elif n < 5:
            answer += n
        #5일 때
        else:
            if (storey//10)%10 > 4:
                storey +=10
            answer += 5
        
        storey //= 10

    return answer
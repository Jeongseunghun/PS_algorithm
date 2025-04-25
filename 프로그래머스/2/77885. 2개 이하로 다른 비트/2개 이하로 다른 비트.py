def solution(numbers):
    answer = []
    for num in numbers:
        #짝수일 때
        if num % 2 == 0:
            answer.append(num+1)
        else:
            b = '0' + bin(num)[2:]
            idx = b.rfind('01')
            b = list(b)
            b[idx], b[idx+1] = '1','0'
            answer.append(int(''.join(b),2))
    return answer
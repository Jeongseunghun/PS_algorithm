def solution(numbers):
    stack = []
    res = [-1] * len(numbers)
    for i in range(len(numbers)):
        tmp = numbers[i]
        while stack and numbers[stack[-1]] < tmp:
            res[stack.pop()] = tmp
        
    
        stack.append(i)
    
    return res
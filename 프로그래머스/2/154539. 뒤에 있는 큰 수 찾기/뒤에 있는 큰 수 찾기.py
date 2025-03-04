def solution(numbers):
    ans = [-1 for _ in range(len(numbers))]
    
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            ans[stack[-1]] = numbers[i]
            stack.pop()
            
        stack.append(i)
        
    return ans
def solution(elements):
    answer = set()
    
    elements.extend(elements)
    
    for l in range(1,len(elements)//2+1):
        for i in range(len(elements)-l+1):
            answer.add(sum(elements[i:i+l]))
    return len(answer)
def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])
    link = set()
    link.add(costs[0][0])
    
    while len(link) != n:
        for s,e,c in costs:
            if s in link and e in link:
                continue
            if s in link or e in link:
                link.update([s,e])
                answer += c
                break

    return answer
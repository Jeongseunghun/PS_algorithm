def solution(gems):
    ans = []
    gem = set(gems)  # 모든 보석 종류
    
    l, r = 0, 0
    gem_count = {}  # 현재 구간의 보석 개수 저장
    
    while r < len(gems):
        # 오른쪽 포인터 확장하며 보석 추가
        gem_count[gems[r]] = gem_count.get(gems[r], 0) + 1
        r += 1
        
        # 모든 보석을 포함하는 경우 → 왼쪽 포인터 이동 가능
        while len(gem_count) == len(gem):
            ans.append([l + 1, r])  # 1-based index
            
            # 왼쪽 포인터가 가리키는 보석 개수 감소
            gem_count[gems[l]] -= 1
            if gem_count[gems[l]] == 0:
                del gem_count[gems[l]]
            l += 1  # 왼쪽 포인터 이동
    
    # 길이가 가장 짧은 구간 반환
    ans.sort(key=lambda x: (x[1] - x[0]))
    return ans[0]
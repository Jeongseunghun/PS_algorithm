from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = defaultdict(int)
    
    # 주문을 정렬하여 조합 생성 시 순서 일관성을 유지
    orders = [''.join(sorted(order)) for order in orders]
    
    # 모든 조합 만들기
    for num in course:
        for order in orders:
            for comb in combinations(order, num):
                menu = ''.join(comb)
                answer[menu] += 1

    # 각 코스 길이에 대해 최댓값을 저장할 딕셔너리
    max_count = {num: 2 for num in course}  # 최소 2번 이상 등장해야 함
    result_by_length = {num: [] for num in course}  # 길이별로 결과 저장

    for key, count in answer.items():
        length = len(key)
        if length in course and count >= 2:  # 부분집합(2번 이상 등장) 필터링
            if count > max_count[length]:  # 최댓값 갱신
                max_count[length] = count
                result_by_length[length] = [key]  # 기존 값 초기화하고 새 값 저장
            elif count == max_count[length]:  # 같은 최댓값이면 추가
                result_by_length[length].append(key)

    # 길이에 따른 조합들을 모두 모아서 정렬 후 반환
    return sorted(sum(result_by_length.values(), []))
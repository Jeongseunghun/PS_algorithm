def solution(plans):
    answer = []

    # plans를 분 단위로 변환하고 시작 시간 기준 정렬
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1].split(":")[0]) * 60 + int(plans[i][1].split(":")[1])
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])

    waiting = []  # 잠시 멈춘 과제 리스트
    current = None  # 현재 진행 중인 과제
    t = 0  # 현재 시간

    while plans or current or waiting:
        # 현재 시간과 같은 시작 시간의 과제 수행
        while plans and plans[0][1] == t:
            name, start, playtime = plans.pop(0)
            if current:
                waiting.append(current)  # 기존 과제 대기열로 이동
            current = [name, playtime]

        # 현재 과제 진행
        if current:
            current[1] -= 1  # 남은 시간 감소
            if current[1] == 0:  # 과제가 끝나면
                answer.append(current[0])
                current = None  # 현재 과제 비우기
                if waiting:
                    current = waiting.pop()  # 대기 중인 과제 바로 수행
        
        t += 1  # 시간 증가

    return answer
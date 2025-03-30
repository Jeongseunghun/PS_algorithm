def solution(n, t, m, timetable):
    # 09:00 => 540분
    start = 540
    
    bus = []
    
    # 각 버스의 출발 시간을 `bus`에 추가
    for i in range(n):
        bus.append(start)
        start += t
    
    # 승객 도착 시간들을 분으로 변환하여 정렬
    timetable = sorted([int(time.split(":")[0]) * 60 + int(time.split(":")[1]) for time in timetable])
    
    # 승객들을 각 버스에 태우기 위한 과정
    last_time = 0  # 마지막 승객의 탑승 시간

    # 각 버스에 승객을 태우기
    for b in bus:
        # 해당 버스에 탑승할 수 있는 승객들
        passengers = 0
        while timetable and timetable[0] <= b and passengers < m:
            last_time = timetable.pop(0)  # 승객이 버스를 타면 마지막 승객 시간이 갱신
            passengers += 1
    
    # 마지막 승객이 탑승한 시간을 기준으로 계산
    if passengers < m:
        # 승객이 남았다면 마지막 버스에 탈 수 있는 시간은 마지막 버스 시간
        last_time = bus[-1]
    else:
        # 마지막 승객이 탑승한 시간을 기준으로 1분 전
        last_time -= 1

    # 시간을 "HH:MM" 형식으로 변환하여 반환
    return f"{last_time // 60:02}:{last_time % 60:02}"
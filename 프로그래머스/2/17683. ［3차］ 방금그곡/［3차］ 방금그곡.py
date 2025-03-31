def solution(m, musicinfos):
    answer = []
    
    # 멜로디 변환 함수
    def convert(mel):
        tmp = []
        for i in range(len(mel) - 1):
            if mel[i] == '#':
                continue
            if mel[i + 1] == '#':
                tmp.append(mel[i:i + 2])
            else:
                tmp.append(mel[i])
        if mel[-1] != '#':
            tmp.append(mel[-1])
        return tmp

    mlst = convert(m)
    
    for info in musicinfos:
        s, e, name, mel = info.split(",")
        st = int(s.split(":")[0]) * 60 + int(s.split(":")[1])
        et = int(e.split(":")[0]) * 60 + int(e.split(":")[1])
        tmp = convert(mel)

        # 멜로디 시간만큼 변환
        melody_time = (tmp * ((et - st) // len(tmp))) + tmp[:((et - st) % len(tmp))]

        # 특정 멜로디(mlst)가 melody_time에 존재하는지 확인
        for i in range(len(melody_time) - len(mlst) + 1):
            cnt = 0  # cnt 초기화
            for j in range(len(mlst)):
                if mlst[j] == melody_time[i + j]:
                    cnt += 1
            if cnt == len(mlst):
                answer.append([st, et, name])
                break

    if not answer:
        return "(None)"
    
    # 정렬 기준: (재생 시간 내림차순, 먼저 입력된 곡 우선)
    answer.sort(key=lambda x: (-(x[1] - x[0]), x[0]))

    return answer[0][2]  # 가장 우선순위 높은 곡 반환
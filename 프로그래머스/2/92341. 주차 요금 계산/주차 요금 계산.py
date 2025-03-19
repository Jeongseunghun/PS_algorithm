import math

def solution(fees, records):
      
    #입출 기록(차량번호 : [시간, 입출 여부])
    record = {}
    
    #자동차별 누적 시간
    cars = {}
    
    for i in records:
        time, carNum, inout = i.split(" ")
        h,m = map(int,time.split(":"))
        
        if carNum not in record:
            cars[carNum] = 0
            record[carNum] = [h*60+m,inout]
        else:
            if record[carNum][1] == 'IN':
                cars[carNum] += (h*60+m) - record[carNum][0]
                record[carNum] = [h*60+m,'OUT']
            else:
                record[carNum] = [h*60+m,'IN']
    
    #in인 차량들 체크
    for i in record:
        if record[i][1] == 'IN':
            cars[i] += (23*60+59) - record[i][0]
    
    ans = []
    for i in cars:
        fee = fees[1]
        #기본시간 이하면 기본 요금
        if fees[0] > cars[i]:
            ans.append([i,fee])
        else:
            fee += math.ceil((cars[i]-fees[0]) / fees[2]) * fees[3]
            ans.append([i,fee])
    
    ans.sort()
    
    res = []
    for i in ans:
        res.append(i[1])

    
    return res
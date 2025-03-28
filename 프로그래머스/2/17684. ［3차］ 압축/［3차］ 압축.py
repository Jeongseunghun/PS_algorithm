def solution(msg):
    answer = []
    
    dict = {}
    for i in range(1,27):
        dict[chr(i+64)] = i
    
    idx = 0
    nxt = 0
    
    while True:
        nxt += 1
        if nxt == len(msg):
            answer.append(dict[msg[idx:nxt]])
            break
        
        if msg[idx:nxt+1] not in dict:
            dict[msg[idx:nxt+1]] = len(dict) + 1
            answer.append(dict[msg[idx:nxt]])
            idx = nxt

    return answer
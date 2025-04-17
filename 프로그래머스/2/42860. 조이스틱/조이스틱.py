def solution(name):
    answer = 0
    N = len(name)
    
    #세로 조작
    for i in name:
        answer += min(ord(i)-ord('A'),ord('Z')-ord(i)+1)
    
    #왼쪽부터 오른쪽 끝까지 커서를 한 번씩 움직이는 경우 최악
    move = N - 1
    
    #현재 위치 i
    for i in range(N):
        #'A'가 아닌 다음 문자 있는 위치
        nxt = i + 1
        #다음 칸이 'A'면 건너 뜀
        while nxt < N and name[nxt] == 'A':
            nxt += 1
        
        #왼쪽갔다가 오른쪽
        move = min(move, 2*i+(N-nxt))
        #오른쪽 갔다가 왼쪽
        move = min(move, i+2*(N-nxt))
    
    answer += move
    
    return answer
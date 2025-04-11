from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    for lst in combinations_with_replacement(range(11),n):
        lion = 0
        peach = 0
        #라이언 점수판
        board = [0 for _ in range(11)]
        for i in lst:
            board[10-i] += 1
        
        for i in range(11):
            #둘다 0점이면 패스
            if info[i] == 0 and board[i] == 0:
                continue
            #라이언이 더 높으면
            elif info[i] < board[i]:
                lion += (10-i)
            #피치가 더 높으면
            else:
                peach += (10-i)
        
        #라이언 점수가 더 크면 answer에 추가
        if peach < lion:
            #[점수차이,라이언 점수판 낮은 점수부터]
            answer.append([lion-peach,board[::-1]])
        
    answer.sort(key = lambda x : (x[0],x[1]), reverse = True)
    
    if len(answer) == 0:
        return [-1]
    return answer[0][1][::-1]
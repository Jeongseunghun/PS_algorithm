def solution(n, k, cmd):
    
    answer = ['O'] * n
    linked_lst = {i: [i-1,i+1] for i in range(n)}
    #삭제된 행 스택
    delete = []
    
    for c in cmd:
        command = c.split()
        
        #X칸 위 행 선택
        if command[0] == 'U':
            for _ in range(int(command[1])):
                k = linked_lst[k][0]
                
        #X칸 아래 행 선택
        elif command[0] == 'D':
            for _ in range(int(command[1])):
                k = linked_lst[k][1]
                
        #현재 선택된 행 삭제, 바로 아래 행 선택
        elif command[0] == 'C':
            prev, nxt = linked_lst[k]
            answer[k] = 'X'
            delete.append([prev,k,nxt])
            
            if nxt == n:
                k = linked_lst[k][0]
            else:
                k = linked_lst[k][1]
            
            if prev == -1:
                linked_lst[nxt][0] = prev
            elif nxt == n:
                linked_lst[prev][1] = nxt
            else:
                linked_lst[prev][1] = nxt
                linked_lst[nxt][0] = prev
            
        #최근 삭제된 행 복구
        elif command[0] == 'Z':
            prev,now,nxt = delete.pop()
            answer[now] = 'O'
            
            if prev == -1:
                linked_lst[nxt][0] = now
            elif nxt == n:
                linked_lst[prev][1] = now
            else:
                linked_lst[prev][1] = now
                linked_lst[nxt][0] = now
    
    return ''.join([i for i in answer])
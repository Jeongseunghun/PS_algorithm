def solution(progresses, speeds):
    ans = []
    lst = []

    for p,s in zip(progresses,speeds):
        if (100-p) % s == 0:
            lst.append((100-p) // s)
        else:
            lst.append((100-p) // s + 1)
    
    start = lst.pop(0)
    cnt = 1
    while lst:
        tmp = lst.pop(0)
        if start < tmp:
            ans.append(cnt)
            cnt = 1
            start = tmp
        else:
            cnt += 1
    
    ans.append(cnt)
    return ans
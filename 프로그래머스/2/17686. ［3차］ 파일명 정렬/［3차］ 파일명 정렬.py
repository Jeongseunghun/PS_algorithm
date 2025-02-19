def solution(files):
    answer = []
    for file in files:
        dict = []
        tmp = []
        for idx,i in enumerate(file):
            if len(dict) == 0:
                if not i.isdigit():
                    tmp.append(i)
                else:
                    dict.append(''.join(tmp))
                    tmp = []
                    tmp.append(i)
            elif len(dict) == 1:
                if i.isdigit():
                    tmp.append(i)
                else:
                    dict.append(''.join(tmp))
                    tmp = []
            else:
                dict.append(file[idx-1:])
                break
        dict.append(''.join(tmp))
        answer.append(dict)
    
    answer.sort(key = lambda x : (x[0].upper(),int(x[1])))
    
    answer = [''.join(i) for i in answer]

    return answer
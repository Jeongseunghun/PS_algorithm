def solution(record):
    dict = {}
    split_record = []
    for i in record:
        split_record.append(i.split(" "))
        
    for i in split_record:
        if i[0] == 'Enter':
            if i[1] not in dict:
                dict[i[1]] = i[2]
            else:
                dict[i[1]] = i[2]
        elif i[0] == 'Change':
            dict[i[1]] = i[2]
    
    ans = []
    for i in split_record:
        if i[0] == 'Enter':
            ans.append("{}님이 들어왔습니다.".format(dict[i[1]]))
        elif i[0] == 'Leave':
            ans.append("{}님이 나갔습니다.".format(dict[i[1]]))
    
    return ans
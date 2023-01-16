T = int(input())
for i in range(T):
    sen = input().replace(' ','')
    cnt = [0]*26
    for i in sen:
        cnt[ord(i)-97] +=1
    
    idx = max(cnt)
    if cnt.count(idx) >=2:
        print("?")
    else:
        print(chr(cnt.index(idx)+97))
            
N = int(input())
num = int(input())
students = list(map(int,input().split()))

paging = {}
for i in range(num):
    #학생이 없으면
    if students[i] not in paging:
        #비어있는 사진틀이 있으면
        if len(paging)< N:
            paging[students[i]] = [1,i]
        #비어있는 사진틀이 없으면
        else:
            #추천 받은 수와 들어온 순서
            lst = sorted(paging.items(), key = lambda x : (x[1][0],x[1][1]))
            tmp = lst[0][0]
            del paging[tmp]
            paging[students[i]] = [1,i]
    #학생이 있으면
    else:
        paging[students[i]][0] += 1        

 
ans = list(sorted(paging.keys()))

for i in ans:
    print(i,end =" ")        
        
        
            
            
        
        
        
    
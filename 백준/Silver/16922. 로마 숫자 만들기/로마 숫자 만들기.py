#문자 순서 X, 중복 O => 중복조합
N = int(input())
lst = [1,5,10,50]
res = []
ans = set()
def back(cnt,num):
    global ans
    if cnt == N:
        ans.add(sum(res))
        return
    for i in range(num,4):
        res.append(lst[i])
        back(cnt+1,i)
        res.pop()

back(0,0)

print(len(ans))
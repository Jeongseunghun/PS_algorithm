N = int(input())
lst = list(map(int,input().split()))

#밑장빼기X 정훈 카드 합
ans = 0
jh = sum(lst[:N:2])

ans = jh
jh_sum = jh

#정훈차례 밑장빼기
for i in range(N-1,0,-2):
    jh_sum += lst[i]
    jh_sum -= lst[i-1]
    ans = max(ans, jh_sum)

jh_sum = jh
#상대차례 밑장빼기
for i in range(N-2,1,-2):
    jh_sum -= lst[i]
    jh_sum += lst[i-1]
    ans = max(ans, jh_sum)

print(ans)


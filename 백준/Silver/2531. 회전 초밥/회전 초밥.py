N,d,k,c = map(int,input().split())
belt = [int(input()) for _ in range(N)]

belt.extend(belt)
max_cb = 0

for i in range(N):
    tmp_lst = belt[i:i+k]
    tmp_lst.append(c)
    tmp_lst = list(set(tmp_lst))
    max_cb = max(max_cb,len(tmp_lst))

print(max_cb)
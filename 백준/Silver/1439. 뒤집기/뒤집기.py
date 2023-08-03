S = input()

cnt_0=0
cnt_1=0

S_0 = S.split("1")
S_1 = S.split("0")

for i in S_0:
    if "0" in i:
        cnt_0 += 1

for i in S_1:
    if "1" in i:
        cnt_1 += 1

print(min(cnt_1,cnt_0))
ans = 0
res = 0
def chk(t):
    if t == "A+":
        s = 4.5
    elif t == "A0":
        s = 4.0
    elif t == "B+":
        s = 3.5
    elif t == "B0":
        s = 3.0
    elif t == "C+":
        s = 2.5
    elif t == "C0":
        s = 2.0
    elif t == "D+":
        s = 1.5
    elif t == "D0":
        s = 1.0
    else:
        s = 0
    return s

for _ in range(20):
    subject,grade,tier = map(str,input().split())
    if tier != 'P':
        s = chk(tier)
        ans += s * float(grade)
        #학점의 총합
        res += float(grade)

print('%.6f' % (ans/res))
jm = list(map(int,input().split()))
gb = list(map(int,input().split()))

jm_score = 0
gb_score = 0
Flag = False

def chk():
    if jm_score > gb_score:
        return True
    else:
        return False

for i in range(9):
    jm_score += jm[i]
    if chk():
        Flag = True
    gb_score += gb[i]
    if chk():
        Flag = True

if Flag:
    print("Yes")
else:
    print("No")
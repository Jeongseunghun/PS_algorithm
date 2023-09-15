S = input()
A_cnt = int(input())

lst = []
dp = [0] * 101
for i in range(A_cnt):
    word = input()
    lst.append(word)

Flag = False

def sol(idx):
    global Flag
    if idx == len(S):
        Flag = True
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for i in range(len(lst)):
        if len(S[idx:]) >= len(lst[i]):
            for j in range(len(lst[i])):
                if S[idx+j] != lst[i][j]:
                    break
            else:
                sol(idx+len(lst[i]))   
    
    return     

sol(0)
if Flag:
    print(1)
else:
    print(0)
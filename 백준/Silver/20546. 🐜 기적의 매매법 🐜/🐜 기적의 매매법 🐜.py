money = int(input())
MD = list(map(int,input().split()))
jh_joo = 0
jh_money = money
sm_joo = 0
sm_money = money
jh_sum = 0
sm_sum = 0

for i in MD:
    if jh_money >=i:
        jh_joo += jh_money // i
        jh_money = jh_money % i
    
jh_sum = jh_money + jh_joo * MD[13]

for i in range(3,len(MD)):
    if sm_money >= MD[i]:
        if MD[i-3] > MD[i-2] > MD[i-1]:
            sm_joo += sm_money // MD[i]
            sm_money = sm_money % MD[i]
    
    elif MD[i-3] < MD[i-2] < MD[i-1]:
        sm_money = sm_money + sm_joo * MD[i]
        sm_joo = 0
    
sm_sum = sm_money + sm_joo * MD[13]


if jh_sum > sm_sum:
    print("BNP")
elif jh_sum < sm_sum:
    print("TIMING")
else:
    print("SAMESAME")
                
            
            


        
        
        
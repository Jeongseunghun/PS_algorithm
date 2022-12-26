coin = int(input())
MD = list(map(int,input().split()))

JH_coin,SM_coin = coin, coin
JH_stock,SM_stock = 0,0


for i in range(14):
    if JH_coin >= MD[i]:
        JH_stock += JH_coin // MD[i]
        JH_coin %= MD[i]


for i in range(11):
    if MD[i] > MD[i+1] > MD[i+2]:
        SM_stock += SM_coin // MD[i+3]
        SM_coin %= MD[i+3]
    
    elif MD[i] < MD[i+1] < MD[i+2]:
        SM_coin += SM_stock * MD[i+3]
        SM_stock = 0
        

JH_asset = [JH_coin + JH_stock * MD[-1]]
SM_asset = [SM_coin + SM_stock * MD[-1]]

if JH_asset > SM_asset:
    print("BNP")
elif JH_asset < SM_asset:
    print("TIMING")
else:
    print('SAMESAME')
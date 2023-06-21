t = int(input())
for _ in range(t):
    N = int(input())
    zero = [1,0]
    one = [0,1]
    if N>1:
        for i in range(N-1):
            zero.append(one[-1])
            one.append(zero[-2]+one[-1])
            
    print(zero[N],one[N])
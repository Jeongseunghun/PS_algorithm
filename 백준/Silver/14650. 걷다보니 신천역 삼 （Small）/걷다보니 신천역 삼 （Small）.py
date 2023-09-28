N = int(input())
res = 0

def make_num(n, sum):
    global res
    for i in range(3):
        if n==0 and i==0:
            continue
        if n==N:
            if sum%3==0:
                res += 1
                return res
        else:
            make_num(n+1, int(str(sum+i)))

make_num(0,0)
print(res)
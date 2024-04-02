n = int(input())

mod = 1000000
p = mod//10*15

a, b = 0, 1
for i in range(n%p):
    a,b = b%mod, (a+b) % mod

print(a)
S = list(input())

zero, one = S.count('0') // 2, S.count('1') // 2

for _ in range(zero):
    S.pop(-S[::-1].index('0') - 1)

for _ in range(one):
    S.pop(S.index('1'))

print(''.join(S))
        
    
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
num = list(str(n + 1))
ml = len(num)
idx = -1

while True:
    if num.count('5') >= k:
        break
    while (num[idx] == '5') and (abs(idx) < ml):
        idx -= 1
    temp = int(''.join(num)) + (10 ** (abs(idx) - 1))
    num = list(str(temp))
    ml = len(num)

print(int(''.join(num)))
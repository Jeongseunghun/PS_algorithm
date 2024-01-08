import sys
input = sys.stdin.readline

word = []

while True:
    s = input().rstrip().split(' ')
    if s[-1] == 'E-N-D':
        break
    for i in s:
        w = ''
        for j in i:
            if('a' <= j < 'z' or 'A' <= j < 'Z' or '-' == j):
                w += j
        word.append(w)

print(max(word,key =lambda x : len(x)).lower())
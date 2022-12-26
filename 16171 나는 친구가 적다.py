S=list(input())
K=input()
new = []

for s in S:
    if ord(s)>=65:
        new.append(s)

new = ''.join(new)

if K in new:
    print(1)
else:
    print(0)

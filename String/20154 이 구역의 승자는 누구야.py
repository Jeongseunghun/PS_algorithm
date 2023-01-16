S= input()
alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
arr = []

for a in S:
    i = ord(a)-ord("A")
    arr.append(alpha[i])

res = sum(arr)%10

if res % 2 ==1:
    print("I'm a winner!")
else:
    print("You're the winner?")
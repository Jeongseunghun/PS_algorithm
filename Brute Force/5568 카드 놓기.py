from itertools import permutations

n=int(input())
k=int(input())
card = []
for i in range(n):
    card.append(input())

ans = set()
for i in permutations(card,k):
    ans.add(''.join(i))


    
print(len(ans))

    
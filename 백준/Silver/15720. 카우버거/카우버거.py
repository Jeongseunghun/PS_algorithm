B,C,D = map(int,input().split())
burger = list(map(int,input().split()))
side = list(map(int,input().split()))
liquid = list(map(int,input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
liquid.sort(reverse=True)

print(sum(burger) + sum(side) + sum(liquid))

min_val = min(B,C,D)

for i in range(min_val):
    burger[i] *= 0.9
    side[i] *= 0.9
    liquid[i] *= 0.9

print(int(sum(burger) + sum(side) + sum(liquid)))
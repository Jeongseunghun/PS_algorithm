import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
while len(lst) > 1:
    tmp = lst.pop() + (lst.pop(0) / 2)
    lst.append(tmp)

print(lst[0])

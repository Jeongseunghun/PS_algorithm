import sys
input = sys.stdin.readline

M = int(input())
ans = set()
for i in range(M):
    a = input().split()
    if len(a) == 1:
        met = a[0]
    else:
        met,n = a
        n = int(n)
    
    if met == "add":
        ans.add(int(n))
    elif met == "remove":
        if n in ans:
            ans.remove(n)
    elif met == "check":
        if n in ans:
            print(1)
        else:
            print(0)
    elif met == "toggle":
        if n in ans:
            ans.remove(n)
        else:
            ans.add(n)
    elif met == "all":
        ans = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif met == "empty":
        ans.clear()
    
    
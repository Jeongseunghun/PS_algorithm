a,b = map(int,input().split())
a_lst = set(map(int,input().split()))
b_lst = set(map(int,input().split()))

ba = b_lst-a_lst
ab = a_lst-b_lst

print(len(ba)+len(ab))
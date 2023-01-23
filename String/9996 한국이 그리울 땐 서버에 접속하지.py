N = int(input())
pat = list(input().split("*"))
length = len(pat[0])+len(pat[1])
for i in range(N):
    dir = input()
    if length > len(dir):
        print("NE")
    else:
        if dir[:len(pat[0])] == pat[0] and dir[-len(pat[1]):] == pat[1]:
            print("DA")
        else:
            print("NE")
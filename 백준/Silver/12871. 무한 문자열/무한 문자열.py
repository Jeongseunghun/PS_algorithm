s = input()
t = input()

s_len = len(s)
t_len = len(t)

s = s*t_len
t = t*s_len

if s == t:
    print(1)
else:
    print(0)
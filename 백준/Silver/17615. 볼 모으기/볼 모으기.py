def move(s,color):
    s = s.lstrip(color)
    return s.count(color)

N = int(input())
color = input()

ans = min(
move(color,"R"),
move(color[::-1],"R"),
move(color,"B"),
move(color[::-1],"B"),
)


print(ans)
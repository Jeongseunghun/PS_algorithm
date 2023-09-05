while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    lst = sorted([a,b,c])
    if lst[2] < lst[0] + lst[1]:
        #세 변의 길이 모두 같을 경우
        if a == b and b == c:
            print('Equilateral')
        #두 변의 길이만 같은 경우
        elif a == b or a == c or b == c:
            print('Isosceles')
        #세 변의 길이 모두 다를 경우
        elif a != b or b != c or a != c:
            print('Scalene')
    else:
        print('Invalid')
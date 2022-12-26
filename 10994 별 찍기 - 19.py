N = int(input())
stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

def fill_star(n,x,y):
    if n == 1:
        stars[y][x] = "*"
        return

    length = 4 * n - 3
    
    for i in range(length):
        stars[y][x+i] = '*'

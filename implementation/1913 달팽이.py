from re import L
from tkinter import N


n = int(input())
loc_n = int(input())

snail = [[0]*n for i in range(n)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

num = n*n
x=0
y=0

while num>0:
    #하
    
    snail[x][y] = num
    num-=1 
    x+=dx[1]
    y+=dy[1]
    
    #우
    snail[x][y] = num
    num-=1
    
    
    
    for i in range(n):
        for j in range(n):
            snail[i][j] = num
            num +=1
    #상
    for i in range(n):
        for j in range(n):
            snail[i][j] = num
            num +=1
    
    
    #좌
    
            
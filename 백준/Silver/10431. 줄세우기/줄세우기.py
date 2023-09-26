P = int(input())

def bubblesort(students):
    global cnt
    for i in range(len(students)-1,0,-1):
        for j in range(i):
            if students[j] > students[j+1]:
                students[j],students[j+1] = students[j+1],students[j]
                cnt+=1

for _ in range(P):
    lst = list(map(int,input().split()))
    students = lst[1:]
    cnt = 0
    bubblesort(students)
    print(lst[0],cnt)
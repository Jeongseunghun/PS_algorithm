K = int(input())
for j in range(1,K+1):
    lst = list(map(int,input().split()))
    num = lst[0]
    score = lst[1:]
    score.sort(reverse=True)
    gap = 0
    for i in range(num-1):
        gap = max(gap,score[i] - score[i+1])
            
    print("Class",j)
    print("Max {0}, Min {1}, Largest gap {2}".format(max(score), min(score), gap))
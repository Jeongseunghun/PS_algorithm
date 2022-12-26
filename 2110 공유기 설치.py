from multiprocessing.connection import answer_challenge


N,C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()

def binary_search(arr,start,end):
    while start<=end:
        mid= (start+end)//2
        current= arr[0]
        cnt=1
        
        for i in range(1,len(arr)):
            if arr[i]>=current+mid:
                cnt+=1
                current=arr[i]
        
        if cnt >= C:
            global answer
            start=mid+1
            answer=mid
        else:
            end = mid- 1

start = 1
end = arr[-1] - arr[0]
answer = 0

binary_search(arr, start, end)
print(answer)
                


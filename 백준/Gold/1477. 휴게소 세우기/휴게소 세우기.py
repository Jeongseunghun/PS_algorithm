import sys
input = sys.stdin.readline
 
n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()
 
start = 1
end = l - 1
 
res = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
 
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > mid:
            count += (arr[i] - arr[i - 1] - 1) // mid
 
    if count > m:
        start = mid + 1
    else:
        res = mid
        end = mid - 1
 
print(res)

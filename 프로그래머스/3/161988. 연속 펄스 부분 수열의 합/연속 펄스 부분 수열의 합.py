def solution(sequence):
    n = len(sequence)
    
    pulse1 = []
    pulse2 = []
    
    for i in range(n):
        if i % 2 == 0:
            pulse1.append(sequence[i])
            pulse2.append(-sequence[i])
        else:
            pulse1.append(-sequence[i])
            pulse2.append(sequence[i])

    def max_subarray(arr):
        max_sum = arr[0]
        current = arr[0]
        for i in range(1, len(arr)):
            current = max(arr[i], current + arr[i])
            max_sum = max(max_sum, current)
        return max_sum

    return max(max_subarray(pulse1), max_subarray(pulse2))
def solution(arr):
    answer = [0,0]
    
    def compress(x,y,size):
        base = arr[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != base:
                    half = size // 2
                    compress(x,y,half)
                    compress(x,y+half, half)
                    compress(x+half,y,half)
                    compress(x+half,y+half,half)
                    return
        answer[base] += 1
    
    compress(0,0,len(arr))
    return answer
        
        
        
    
    return answer
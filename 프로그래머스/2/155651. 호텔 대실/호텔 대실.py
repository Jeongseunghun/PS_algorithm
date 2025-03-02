import heapq

def solution(book_time):
    for i in range(len(book_time)):
        book_time[i][0] = str(''.join(book_time[i][0].split(":")))
        book_time[i][0] = int(book_time[i][0][:2]) * 60 + int(book_time[i][0][2:])
        book_time[i][1] = str(''.join(book_time[i][1].split(":")))
        book_time[i][1] = int(book_time[i][1][:2]) * 60 + int(book_time[i][1][2:])
    
    book_time.sort(key = lambda x: x[0])
    room = []
    ans = 0
    
    for s,e in book_time:  
        if room and room[0] <= s:
            heapq.heappop(room)
        else:
            ans+=1
        
        heapq.heappush(room,e+10)
    
    return ans
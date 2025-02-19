from collections import deque

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        lst = {'a':'bc','b':'ac','c':'ab'}
        q = deque(['a','b','c'])

        while len(q[0]) != n:
            u = q.popleft()
            for i in lst[u[-1]]:
                q.append(u+i)
        
        return '' if len(q) < k else q[k-1]
            

            
            
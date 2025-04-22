from itertools import product

def solution(word):
    w = ['A','E','I','O','U']
    
    lst = []
    for i in range(1,6):
        for x in product(w,repeat = i):
            lst.append(''.join(x))
    
    lst.sort()
    for idx,i in enumerate(lst):
        if i == word:
            return idx+1
            
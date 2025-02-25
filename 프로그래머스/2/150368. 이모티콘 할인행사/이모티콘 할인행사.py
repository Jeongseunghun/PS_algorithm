from itertools import product

def solution(users, emoticons):
    sale_lst = [10,20,30,40]
    
    lst = []
    
    for sales in product(sale_lst,repeat = len(emoticons)):
        emtiple = 0
        money = 0
        for user in users:
            total = 0
            for idx,i in enumerate(sales):
                if user[0] <= sales[idx]:
                    total += emoticons[idx]*(100-i)//100
            if total >= user[1]:
                emtiple += 1
            else:
                money += total
        lst.append([emtiple,money])
    
    lst = sorted(lst,key = lambda x: (-x[0],-x[1]))
        
    
    return lst[0]
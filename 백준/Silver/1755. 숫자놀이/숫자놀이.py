m,n = map(int,input().split())
alpha = {'0':'zero','1':'one', '2':'two', '3':'three','4': 'four', '5':'five', '6':'six','7':'seven','8':'eight','9':'nine','10':'ten' }

lst= []
for i in range(m,n+1):
    a = ' '.join([alpha[j] for j in str(i)])
    lst.append([i,a])

lst.sort(key = lambda x:x[1])

for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print(sep = '\n')
    print(lst[i][0], end = ' ')
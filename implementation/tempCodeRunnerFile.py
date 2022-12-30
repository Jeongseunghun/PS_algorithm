n = input()
duck = n.split('k')

cry = ['q','u','a','c','k']
cnt = [0,0,0,0,0]
res = []

if len(n) % 5 !=0 or n[0] != "q":
    print(-1)
    exit()

for i in range(len(duck)):
    res.append(duck[i].count("q"))

for i in n:
    for j in range(len(cry)):
        if i == cry[j]:
            cnt[j] +=1
        for k in range(len(cnt)):
            for l in range(k,len(cnt)):
                if cnt[k] < cnt[l]:
                    print(-1)
                    exit()


            


print(max(res))
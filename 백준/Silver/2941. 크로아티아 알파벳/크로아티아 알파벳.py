s = input()
cnt = 0
dict = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',"m"
       ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in dict:
    if s.count(i) >= 1:
        cnt += s.count(i)
        s = s.replace(i," ")

for j in alpha:
    if s.count(j) >= 1:
        cnt += s.count(j)
        s = s.replace(j, " ")

print(cnt)
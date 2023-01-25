n=input().split('-')
val=0
for i in n[0].split('+'):
    val += int(i)
for i in n[1:]:
    for j in i.split('+'):
        val -= int(j)
print(val)
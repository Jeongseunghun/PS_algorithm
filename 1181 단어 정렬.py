N = int(input())
s=set(input() for _ in range(N))
Sol=list(s)

Sol.sort()
Sol.sort(key=len)

for i in Sol:
    print(i)
    

    
    
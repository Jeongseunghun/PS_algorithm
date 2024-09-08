N = int(input())
lst = list(map(int,input().split()))
lst.sort()
ans = 0

for i in range(N-2):
    s = i+1
    e = N-1
    while s<e:
        m = lst[s] + lst[e]
        if m == -lst[i]:
            if lst[s] == lst[e]:
                ans += e-s
                s+=1
            else:
                j,k = s,e
                while lst[j] == lst[s] and j<e:
                    j+=1
                while lst[k] == lst[e] and k>s:
                    k-=1
                ans += (j-s)*(e-k)
                s,e = j,k
        elif m < -lst[i]:
            s+=1
        else:
            e-=1

print(ans)
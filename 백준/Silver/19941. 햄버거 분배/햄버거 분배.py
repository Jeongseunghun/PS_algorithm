N,K = map(int,input().split())
s = list(input())

max_ham = 0
for i in range(N):
    if s[i] == 'P':
        for j in range(i-K,i+K+1):
            if 0 <= j < N and s[j] == 'H':
                max_ham+=1
                s[j] = 'E'
                break

print(max_ham)
s = input()

word = s

for i in range(1,len(s)):
    for j in range(i+1,len(s)):
        word = min(word,s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])

print(word)
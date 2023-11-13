doc = input()
word = input()

doc_len = len(doc)
if word in doc:
    doc = doc.replace(word,'')

cnt = (doc_len - len(doc)) // len(word)
        
print(cnt)
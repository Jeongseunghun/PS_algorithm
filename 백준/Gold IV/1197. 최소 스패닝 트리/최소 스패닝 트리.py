#Kruskal

V,E = map(int,input().split())

#root를 저장
root = [i for i in range(V+1)]

lst = []
for _ in range(E):
    lst.append(list(map(int,input().split())))

#가중치 기준 정렬
lst.sort(key=lambda x : x[2])


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

ans = 0
#간선 리스트 순회
for a,b,c in lst:
    #시작 정점 a의 root 찾기
    sRoot = find(a)
    #끝 정점 b의 root 찾기
    eRoot = find(b)
    #시작 정점과 끝 정점의 root가 같지 않아야 사이클 형성 X
    if sRoot != eRoot:
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] = sRoot
        ans += c

print(ans)
def recursive(root,start,end):
    for i in range(start,end):
        #전위의 루트는 첫 번째
        if inorder[i] == preorder[root]:
            recursive(root+1,start,i)
            recursive(root+i+1-start,i+1,end)
            print(preorder[root], end = " ")
            


T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    recursive(0,0,n)
    print("")
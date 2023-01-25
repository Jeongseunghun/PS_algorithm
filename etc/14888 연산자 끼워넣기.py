# N = int(input())
# cnt = list(map(int,input().split()))
# # +:0, -:1, *:2, //:3
# oper = list(map(int,input().split()))

# max_value = -1e9
# min_value = 1e9

# def calc(depth, sum, plus, minus, multiply, divide):
#     global max_value,min_value
    
#     if depth == N:
#         max_value = max(sum,max_value)
#         min_value = min(sum,min_value)
#         return 

#     if plus:
#         calc(depth+1, sum + cnt[depth], plus-1, minus, multiply, divide)
#     if minus:
#         calc(depth+1, sum - cnt[depth], plus, minus-1, multiply, divide)
#     if multiply:
#         calc(depth+1, sum * cnt[depth], plus, minus, multiply-1, divide)
#     if divide:
#         calc(depth+1, int(sum / cnt[depth]), plus, minus, multiply, divide-1)


# calc(1,cnt[0],oper[0],oper[1],oper[2],oper[3])
# print(max_value)
# print(min_value)

print(int(-2//3))
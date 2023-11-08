N, M = map(int, input().split())
basket_list = [i for i in range(1, N+1)]

for _ in range(M):
    i,j = map(int, input().split())
    temp = basket_list[i-1:j]
    temp.reverse()
    basket_list[i-1:j] = temp

for i in range(N):
    print(basket_list[i], end=" ")
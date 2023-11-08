N, M = map(int, input().split())

ball_list = [0]*N
for _ in range(1, M+1):
    i, j, k = map(int, input().split())

    for _ in range(j-i+1):
        ball_list.insert(i-1, k)
        ball_list.pop(j)
for _ in range(N):
    print(ball_list[_], end=" ")
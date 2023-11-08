N, M = map(int, input().split())

ball_list = [0]*N
for q in range(1, M+1):
    i, j, k = map(int, input().split())

    for p in range(j-i+1):
        ball_list.insert(i-1, k)
        ball_list.pop(j)
for a in range(N):
    print(ball_list[a], end=" ")
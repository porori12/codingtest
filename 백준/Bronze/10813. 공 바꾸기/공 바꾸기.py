N, M = map(int, input().split())
ball_list = [i for i in range(1, N+1)]

temp = []
for _ in range(M):
    i,j = map(int, input().split())
    temp = ball_list[i-1]
    ball_list[i-1] = ball_list[j-1]
    ball_list[j-1] = temp

for i in range(N):
    print(ball_list[i], end=" ")
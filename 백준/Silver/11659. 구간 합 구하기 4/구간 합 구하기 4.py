import sys

input = sys.stdin.readline

N, M = map(int, input().split())
input_list = list(map(int, input().split()))

dp = [0] * (N + 1)

for _ in range(N):
    dp[_+1] = dp[_] + input_list[_]

for i in range(M):
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])
N = int(input())
dp = [0] * (N+1)
dp[0] = 2
for i in range(1, N+1):
    dp[i] = (dp[i-1]) * 2 - 1

print(dp[i]**2)
A, B = map(int, input().split())

dp = []

for i in range(1, B+1):
    for j in range(i):
        dp.append(i)

result = sum(dp[A-1:B])

print(result)
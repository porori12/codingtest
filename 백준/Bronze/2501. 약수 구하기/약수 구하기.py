N, K = map(int, input().split())
answer = []

for i in range(1, N+1):
    if N % i == 0:
        answer.append(i)

answer.sort()

if len(answer) < K:
    result = 0
else:
    result = answer[K-1]
    
print(result)
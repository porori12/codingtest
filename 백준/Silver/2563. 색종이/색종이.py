N = int(input())
rows = 100
cols = 100
arr = [[0 for j in range(cols)] for i in range(rows)]

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1

sum_result = 0

for p in arr:
    sum_result += sum(p)

print(sum_result)
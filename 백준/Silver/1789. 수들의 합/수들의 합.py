import sys

n = int(sys.stdin.readline())

sum = 0
result = 0

for i in range(1, n+1):
    sum = sum + i
    result += 1
    if sum > n:
        result = result - 1
        break

print(result)
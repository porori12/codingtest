import math

N, M = map(int, input().split())

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

result = binomial_coefficient(N, M)
print(result)
N = int(input())
M = str(input())

sum_result = 0
for i in range(0, N):
    A = ((M[i:i+1]))
    int_A = int(A)
    sum_result += int_A

print(sum_result)
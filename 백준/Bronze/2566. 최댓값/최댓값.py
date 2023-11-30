li = []
max_value = []

for _ in range(9):
    N = list(map(int, input().split()))
    li.append(N)

for i in range(9):
    max_value.append(max(li[i]))
A = max(max_value)
print(A)
print(max_value.index(max(max_value)) + 1, li[max_value.index(A)].index(max(li[max_value.index(A)])) + 1)

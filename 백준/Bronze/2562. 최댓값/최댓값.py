value_list = []

for i in range(1, 10):
    A = int(input())
    value_list.append(A)

max_value = max(value_list)
print(max_value)
C = value_list.index(max_value)+1
print(C)
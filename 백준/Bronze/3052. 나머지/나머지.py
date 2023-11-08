num_list = []
for _ in range(10):
    A = int(input())%42
    num_list.append(A)
output = dict.fromkeys(num_list)
output2 = list(output)
print(len(output2))
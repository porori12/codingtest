white_list = [1, 1, 2, 2, 2, 8]
input_list = list(map(int, input().split()))
output_list = [0]* len(white_list)

for i in range(len(white_list)):
    output_list[i] = (white_list[i]-input_list[i])

print(*output_list)
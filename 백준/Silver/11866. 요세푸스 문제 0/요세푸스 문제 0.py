N, K = list(map(int, input().split()))
N_list = list(range(1, N+1))

idx = 0
output_list = []

while N_list:
    idx += K-1
    if idx >= len(N_list):
        idx %= len(N_list)
    output_list.append(str(N_list.pop(idx)))

print("<", ", ".join(output_list), ">", sep="")
N = int(input())
N_li = list(map(int, input().split()))

if max(N_li) % 2 == 0:
    print(2 * max(N_li))
else:
    print(max(N_li) * min(N_li))
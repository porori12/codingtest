n, k = map(int, input().split())
coin_list = []
cnt = 0

for _ in range(n):
    _ = int(input())
    coin_list.append(_)
    coin_list.sort(reverse=True)

for coin in coin_list:
    if k >= coin:
        cnt += k // coin
        k %= coin
        if k <= 0:
            break

print(cnt)



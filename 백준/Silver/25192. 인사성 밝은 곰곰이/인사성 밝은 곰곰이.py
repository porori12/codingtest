from sys import stdin

input = stdin.readline

N = int(input())

gomgom = set()
cnt = 0

for i in range(N):
    msg = input().strip()
    if msg == "ENTER":
        cnt += len(gomgom)
        gomgom = set()

    else:
        gomgom.add(msg)
cnt += len(gomgom)
print(cnt)

import sys

N, M = map(int, input().split())

stored_dicts = dict()
cnt = 0

for i in range(N):
    dicts = sys.stdin.readline().strip()
    stored_dicts[dicts] = i + 1

for j in range(M):
    dicts = sys.stdin.readline().strip()
    if dicts in stored_dicts:
        cnt += 1

print(cnt)


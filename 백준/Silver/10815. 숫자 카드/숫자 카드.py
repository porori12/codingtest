import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

my_dict = {}
for i in range(len(cards)):
    my_dict[cards[i]] = 0

for j in range(M):
    if checks[j] not in my_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')

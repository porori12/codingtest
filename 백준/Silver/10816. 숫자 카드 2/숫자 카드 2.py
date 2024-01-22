from sys import stdin
from collections import Counter

N = stdin.readline()
card = list(map(int, stdin.readline().split()))
M = stdin.readline()
test = list(map(int, stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end= ' ')
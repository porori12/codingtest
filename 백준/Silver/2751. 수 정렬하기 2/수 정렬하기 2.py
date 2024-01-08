import sys


N = int(input())
li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()

for i in li:
    print(i)
import sys

N, M = map(int, sys.stdin.readline().split())
pocketmonIntKey = {}
pocketmonStrKey = {}


for i in range(N):
    pocketmonName = sys.stdin.readline().strip()
    pocketmonIntKey[i] = pocketmonName
    pocketmonStrKey[pocketmonName] = i

for _ in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(pocketmonIntKey[int(question) - 1])
    else:
        print(pocketmonStrKey[question] + 1)

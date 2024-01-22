from sys import stdin

N, M = map(int, stdin.readline().split())
strange_name = set()
input_name = set()
result = []


for _ in range(N):
    strange_name.add(stdin.readline().rstrip())

for _ in range(M):
    input_name.add(stdin.readline().rstrip())


for i in input_name:
    if i in strange_name:
        result.append(i)

result.sort()
print(len(result))
for j in result:
    print(j)
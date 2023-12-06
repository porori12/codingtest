N = int(input())
result = []

for i in range(N):
    li = list(map(int, input().split()))
    result.append(li)

result.sort()
for i in result:
    print(i[0], i[1])
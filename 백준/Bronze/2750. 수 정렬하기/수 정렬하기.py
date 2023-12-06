N = int(input())
li = []

for i in range(N):
    N = int(input())
    li.append(N)
li.sort(reverse=False)
for _ in li:
    print(_)
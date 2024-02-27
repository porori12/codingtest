inputList = []

for i in range(7):
    A = int(input())
    if A % 2 == 1:
        inputList.append(A)

if not inputList:
    print(-1)
else:
    print(sum(inputList))
    print(min(inputList))

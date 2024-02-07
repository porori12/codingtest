from sys import stdin

input = stdin.readline

N = int(input())

result = []

for _ in range(N):
    command = list(map(str, input().rstrip().split()))
    if command[0] == "push":
        result.append(command[1])
    elif command[0] == "pop":
        if not result:
            print(-1)
        else:
            print(result.pop())
    elif command[0] == "size":
        print(len(result))
    elif command[0] == "empty":
        if not result:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if not result:
            print(-1)
        else:
            print(result[-1])
from sys import stdin
from collections import deque



input = stdin.readline

N = int(input())

result = deque()

for _ in range(N):
    command = list(map(str, input().rstrip().split()))
    if command[0] == "push_front":
        result.appendleft(command[1])
    elif command[0] == "push_back":
        result.append(command[1])
    elif command[0] == "pop_front":
        if not result:
            print(-1)
        else:
            print(result.popleft())
    elif command[0] == "pop_back":
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
    elif command[0] == "front":
        if not result:
            print(-1)
        else:
            print(result[0])
    elif command[0] == "back":
        if not result:
            print(-1)
        else:
            print(result[-1])
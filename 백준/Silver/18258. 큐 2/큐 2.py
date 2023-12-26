from sys import stdin
from collections import deque

N = int(input())
stack = deque([])

for _ in range(N):
    command = stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if stack:
            print(stack.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])


    elif command[0] == 'back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])



from sys import stdin
from collections import deque

N = int(input())
stack = deque([])

for _ in range(N):
    command = stdin.readline().split()

    if command[0] == '1':
        stack.appendleft(command[1])

    elif command[0] == '2':
        stack.append(command[1])

    elif command[0] == '3':

        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(stack))
    elif command[0] == '6':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == '7':

        if stack:
            print(stack[0])
        else:
            print(-1)

    elif command[0] == '8':
        if stack:
            print(stack[-1])
        else:
            print(-1)




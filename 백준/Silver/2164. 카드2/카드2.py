from collections import deque

N = int(input())
my_str = deque(list(range(1, N+1)))

while (len(my_str) > 1):
    my_str.popleft()
    temp = my_str.popleft()
    my_str.append(temp)

print(my_str[0])
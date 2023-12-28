import sys

P = int(input())
S = set()

for _ in range(P):
    temp = sys.stdin.readline().strip().split()


    if len(temp) == 1:
        if temp[0] == "all":
            S = set(i for i in range(1, 21))
        else:
            S = set()

    else:
        if temp[0] == 'add':
            S.add(int(temp[1]))
        elif temp[0] == 'remove':
            S.discard(int(temp[1]))
        elif temp[0] == 'check':
            if int(temp[1]) in S:
                print(1)
            else:
                print(0)
        elif temp[0] == 'toggle':
            if int(temp[1]) in S:
                S.discard(int(temp[1]))
            else:
                S.add(int(temp[1]))

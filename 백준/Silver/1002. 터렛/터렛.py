T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    X = abs((x1 - x2) ** 2)
    Y = abs((y1 - y2) ** 2)

    XY = (X + Y) ** (1/2)
    R = abs(r1 - r2)

    if XY == 0 and r1 == r2:
        print(-1)
    elif R == XY or (r1 + r2) == XY:
        print(1)
    elif R < XY < (r1 + r2):
        print(2)
    else:
        print(0)
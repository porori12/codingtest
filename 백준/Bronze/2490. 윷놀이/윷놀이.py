for i in range(3):
    yut = list(map(int, input().split()))
    result = sum(yut)

    if result == 3:
        print("A")
    elif result == 2:
        print("B")
    elif result == 1:
        print("C")
    elif result == 0:
        print("D")
    elif result == 4:
        print("E")
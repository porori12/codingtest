while True:
    angle_list = []
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    angle_list = [a, b, c]
    angle_list.sort()

    if angle_list[2] >= angle_list[1] + angle_list[0]:
        print("Invalid")
    else:
        if angle_list[0] == angle_list[2]:
            print("Equilateral")
        elif angle_list[0] == angle_list[1] or angle_list[1] == angle_list[2]:
            print("Isosceles")
        else:
            print("Scalene")

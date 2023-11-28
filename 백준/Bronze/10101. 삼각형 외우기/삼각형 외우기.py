angle = 0
angle_list = []

for i in range(3):
    a = int(input())
    angle_list.append(a)
    angle += a

if angle != 180:
    print("Error")
else:
    if angle_list[0] == angle_list[1] == angle_list[2]:
        print("Equilateral")
    elif angle_list[0] == angle_list[1] or angle_list[1] == angle_list[2] or angle_list[0] == angle_list[2]:
        print("Isosceles")
    else:
        print("Scalene")
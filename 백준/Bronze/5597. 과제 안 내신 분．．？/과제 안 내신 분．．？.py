student_list = [i for i in range(1, 30+1)]

for _ in range(1, 29):
    student_num = int(input())
    student_list.remove(student_num)

print(min(student_list))
print(max(student_list))
from sys import stdin
# import statistics as st

input = stdin.readline

N = int(input())
num = 0
li = []

for i in range(N):
    num = int(input())
    li.append(num)
li.sort(reverse=False)

print(round(sum(li)/N))
# print(st.median(li))
print(li[N//2])

my_dict = dict()

for input_num in li:
    if input_num in my_dict:
        my_dict[input_num] = my_dict[input_num] + 1
    else:
        my_dict[input_num] = 1

freq = max(my_dict.values())
numbers = []

for key, value in my_dict.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

print(li[-1] - li[0])
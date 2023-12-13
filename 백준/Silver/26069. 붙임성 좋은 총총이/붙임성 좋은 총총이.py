from sys import stdin

input = stdin.readline

N = int(input())
a = 0
b = 0

dance_list = set()
dance_list.update(['ChongChong'])

for _ in range(N):
    a, b = list(map(str, input().split()))
    if a in dance_list or b in dance_list:
        dance_list.add(a)
        dance_list.add(b)
        dance_list = set(dance_list)
        
    else:
        continue
print(len(dance_list))
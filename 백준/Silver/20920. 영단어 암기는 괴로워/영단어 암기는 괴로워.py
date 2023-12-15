from sys import stdin
input_s = stdin.readline
N, M = map(int, input().split())

li = []
my_word = 0

for i in range(N):
    my_word = str(input_s()).rstrip()
    if len(my_word) >= M:
        li.append(my_word)

my_dictonary = dict()
for word in li:
    if word not in my_dictonary:
        my_dictonary[word] = [1, len(word), word]
    else:
        my_dictonary[word][0] = my_dictonary[word][0] + 1

ans = sorted(my_dictonary.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in ans:
    print(a[0])

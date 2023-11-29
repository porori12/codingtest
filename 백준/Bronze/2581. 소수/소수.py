M = int(input())
N = int(input())
result = 0
re_li = []

for i in range(M, N+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            result += i
            re_li.append(i)

if len(re_li) == 0:
    print("-1")
else:
    print(result)
    print(min(re_li))

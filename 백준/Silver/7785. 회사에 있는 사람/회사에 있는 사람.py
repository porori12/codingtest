import sys

n = int(sys.stdin.readline())
inCompany = dict()

for _ in range(n):
    tem, tem_state = map(str, sys.stdin.readline().split())

    if tem_state == 'enter':
        inCompany[tem] = tem_state
    else:
        del inCompany[tem]

answer = sorted(inCompany.keys(), reverse=True)

for j in answer:
    print(j)
T = int(input())

for i in range(T):
    r, s = input().split()
    R = int(r)
    S = str(s)
    for _ in range(len(S)):
        print(S[_] * R, end='')
    print()
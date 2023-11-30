T = int(input())

for i in range(T):
    Q = 0
    D = 0
    N = 0
    P = 0
    C = int(input())
    while C >= 25:
        C -= 25
        Q += 1
    while C >= 10:
        C -= 10
        D += 1
    while C >= 5:
        C -= 5
        N += 1
    while C >= 1:
        C -= 1
        P += 1

    print(Q, D, N, P)
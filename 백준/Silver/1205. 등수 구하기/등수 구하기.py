N, newScore, P = map(int, input().split())
scoreList = []

if N == 0:
    print(1)
else:
    scoreList = list(map(int, input().split()))
    if N == P and newScore <= scoreList[-1]:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if scoreList[i] <= newScore:
                result = i + 1
                break

        print(result)
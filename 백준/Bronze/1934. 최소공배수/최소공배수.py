N = int(input())


for j in range(N):
    a, b = map(int, input().split())
    for i in range(min(a,b), 0, -1):
        answer = 0
        if a%i == 0 and b%i == 0:
            answer = i
            break
    print((a*b)//i)

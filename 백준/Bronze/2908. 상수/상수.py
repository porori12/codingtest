A, B = map(str, input().split())

a, b = int(A[::-1]), int(B[::-1])

if a > b:
    print(a)
else:
    print(b)
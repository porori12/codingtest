a, b = map(int, input().split())
damage = a - (a/100 * b)
if damage >= 100:
    print("0")
else:
    print("1")
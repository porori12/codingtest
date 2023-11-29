while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    result = 0
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
            result += i
        else:
            continue

    if n == result:
        di = " + ".join(map(str, arr))
        print(f'{n} = {di}')
    else:
        print(f'{n} is NOT perfect.')
P = int(input())

for _ in range(P):
    arr = list(map(int, input().split()))
    total_value = 0

    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                total_value += 1

    print(arr[0], total_value)





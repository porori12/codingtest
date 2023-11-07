N = int(input())

if 4 <= N <= 1000 and N % 4 ==0:
    for i in range(1, N//4 + 1):
        print('long ' ,end="")
    print('int')

else:
    print("ValueError!")
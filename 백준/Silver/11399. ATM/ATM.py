N = int(input())

peopleList = list(map(int, input().split()))
peopleList.sort()

waitingTime = [0] * len(peopleList)

waitingTime[0] = peopleList[0]

for _ in range(1, len(peopleList)):
    waitingTime[_] = waitingTime[_ - 1] + peopleList[_]

print(sum(waitingTime))
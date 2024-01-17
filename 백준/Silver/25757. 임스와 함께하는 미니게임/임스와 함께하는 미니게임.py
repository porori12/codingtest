numberOfPeople, game = input().split()
numberOfPeople = int(numberOfPeople)
peopleNameList = []

for _ in range(numberOfPeople):
    peopleName = str(input())
    peopleNameList.append(peopleName)

peopleNameList = list(set(peopleNameList))

if game == 'Y':
    print(len(peopleNameList))
elif game == 'F':
    print(len(peopleNameList) // 2)
elif game == 'O':
    print(len(peopleNameList) // 3)
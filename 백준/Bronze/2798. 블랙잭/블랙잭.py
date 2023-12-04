from itertools import permutations, combinations, combinations_with_replacement

N, M = map(int, input().split())

card = list(map(int, input().split()))
li = []
result = []
for i in range(N):
    li = list(combinations(card, 3))

for j in range(len(li)):
    if M >= (sum(li[j])):
        result.append(sum(li[j]))
print(max(result))

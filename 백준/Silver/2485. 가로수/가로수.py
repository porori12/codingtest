
from math import gcd

N = int(input())
arr = []
arr2 = []
result = []

for _ in range(N):
    put = int(input())
    arr.append(put)

for i in range(len(arr)-1):
    put2 = arr[i+1] - arr[i]
    arr2.append(put2)

g = arr2[0]
for j in range(1, len(arr2)):
    g = gcd(g, arr2[j])
    result.append(arr2[0])
    result.append(g)

trees = (arr[-1]-arr[0])//min(result)
existing_tree = len(arr) - 1
print(trees - existing_tree)
S = str(input())
A = ""
B = ""
result = 0
for i in reversed(S):
    A += i

for i in S:
    B += i

for _ in range(1, (2*len(S)-1)):
    if A == B:
        result += 0
    else:
        result += 1

if result == 0:
    print("1")
else :
    print("0")
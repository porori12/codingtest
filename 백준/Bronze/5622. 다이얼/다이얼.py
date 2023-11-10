S = str(input())

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for j in range(len(S)):
    for i in dial:
        if S[j] in i:
            result += dial.index(i)+3
            
print(result)
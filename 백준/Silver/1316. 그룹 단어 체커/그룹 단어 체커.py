N = int(input())
cnt = 0

for i in range(N):
    word = input()
    result = []
    if len(word) == 1:
        cnt += 1
    else:
        for j in range(len(word)):
            if j == 0:
                result.append(word[0])
            elif j > 0:
                if word[j] == word[j-1]:
                    result.append(word[j])
                    if j == len(word)-1:
                        cnt += 1

                elif word[j] != word[j-1]:
                    if word[j] not in result:
                        if j == len(word)-1:
                            cnt += 1
                        else:
                            result.append(word[j])
                    elif word[j] in result:
                        break
print(cnt)
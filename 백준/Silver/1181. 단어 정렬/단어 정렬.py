n = int(input())
result = []


for _ in range(n):
    word = str(input())
    result.append((len(word), word))
result = list(set(result))
result.sort()


for word_len, word in result:
    print(word)
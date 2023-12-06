li = []

for i in range(5):
    N = int(input())
    li.append(N)

print(sum(li)//5)
li.sort(reverse=True)
print(li[2])
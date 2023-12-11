import math

a, b = map(int, input().split())
c, d = map(int, input().split())
sum_1 = int(math.lcm(b,d))
# print(int((math.lcm(b,d)/b * a + math.lcm(b,d)/d * c)), math.lcm(b,d))

answer_1 = int((math.lcm(b,d)/b * a + math.lcm(b,d)/d * c))
answer_2 = math.lcm(b,d)
answer = math.gcd(answer_1, answer_2)

print(answer_1//answer, answer_2//answer)
N = int(input())

subject_score = list(map(int, input().split()))

M = max(subject_score)
result = 0
for i in range(N):
    af_score = subject_score[i]/M * 100
    result += af_score

af_average = result/N
print(af_average)
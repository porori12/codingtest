a_result = []
b_result = []

for i in range(3):
    a, b = map(int, input().split())
    a_result.append(a)
    b_result.append(b)

a_count = {} # 각 원소의 등장 횟수를 카운팅할 딕셔너리
b_count = {}

for i in a_result:
    try: # 이미 등장한 값의 경우
        a_count[i] += 1
    except: # 처음 등장한 값의 경우
        a_count[i] = 1

for j in b_result:
    try:
        b_count[j] += 1
    except:
        b_count[j] = 1

result = []
for k, v in a_count.items():
    if v == 1: # n회 이상 등장한 원소로도 변경 가능
        result.append(k)

for k_2, v_2 in b_count.items():
    if v_2 == 1:
        result.append(k_2)

for x in result:
    print(x, end= " ")
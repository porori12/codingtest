import sys
input = sys.stdin.readline
N = int(input())
sub = []

for _ in range(N):
    sub.append(list(input().split()))
    
sub.sort(key=lambda a:int(a[0]))

for i in range(N):
    print(sub[i][0], sub[i][1])
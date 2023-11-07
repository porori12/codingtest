import sys

input = sys.stdin.readline

N = int(input())
int_list = list(map(int, input().split()))
v = int(input())

print(int_list.count(v))
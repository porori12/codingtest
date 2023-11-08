import sys

input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))

print(min(input_list), max(input_list))
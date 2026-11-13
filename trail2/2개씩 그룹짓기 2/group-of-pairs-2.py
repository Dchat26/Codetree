import sys
input = sys.stdin.readline

N = int(input())
a = sorted(map(int, input().split()))

print(min(a[i + N] - a[i] for i in range(N)))
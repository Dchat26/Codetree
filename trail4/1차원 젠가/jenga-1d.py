import sys
input = sys.stdin.readline

n = int(input())
nlist = [int(input()) for _ in range(n)]

for _ in range(2):
    b, c = map(int, input().split())
    del nlist[b-1:c]

print(len(nlist))
if nlist:
    print('\n'.join(map(str, nlist)))
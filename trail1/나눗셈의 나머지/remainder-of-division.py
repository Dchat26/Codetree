a, b = map(int, input().split())

answer = [0] * 10
while a > 1:
    answer[a % b] += 1
    a //= b

print(sum(i * i for i in answer))
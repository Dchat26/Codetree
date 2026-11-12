n = int(input())
arr = list(input().split())

answer = 0
while True:
    is_TF = True
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            is_TF = False
            answer += 1
    
    if is_TF:
        break

print(answer)
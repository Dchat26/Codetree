a, b = input().split()
b = int(b)

result = list(a)
for _ in range(b):
    i, j, k = input().split()

    if i == '1':
        result[int(j)-1], result[int(k)-1] = result[int(k)-1], result[int(j)-1]
    else:
        temp = result
        for idx, i in enumerate(result):
            if i == j:
                temp[idx] = k
        
        result = temp
    
    print("".join(result))
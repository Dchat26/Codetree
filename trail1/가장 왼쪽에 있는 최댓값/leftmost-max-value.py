a = int(input().rstrip())

alist = list(map(int, input().split()))

while True:
    max_index = alist.index(max(alist))

    print(max_index + 1, end=' ')

    if alist[max_index] == alist[0]:
        break
    
    alist = alist[:max_index]
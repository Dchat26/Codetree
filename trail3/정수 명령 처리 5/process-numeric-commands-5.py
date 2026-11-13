N = int(input())

array = []
for _ in range(N):
    s = input().split()

    if len(s) == 2:
        a, b = s[0], s[1]
        b = int(b)

        if a == "push_back":
            array.append(b)
        else:
            print(array[b-1])
    else:
        if s[0] == "size":
            print(len(array))
        else:
            array.pop()
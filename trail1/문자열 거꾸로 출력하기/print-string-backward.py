while True:
    a = input().rstrip()

    if a == "END":
        break
    
    print(a[::-1])
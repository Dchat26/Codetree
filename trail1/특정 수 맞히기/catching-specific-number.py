while True:
    a = int(input().rstrip())

    if a < 25:
        print("Higher")
    elif a > 25:
        print("Lower")
    elif a == 25:
        print("Good")
        break
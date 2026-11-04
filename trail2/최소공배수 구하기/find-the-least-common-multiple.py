def gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


def lcm(a, b, c):
    print(a * b // c)


a, b = map(int, input().split())

lcm(a, b, gcd(a, b))
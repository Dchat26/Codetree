X = int(input())

def max_dist(T):
    k = T // 2
    if T % 2 == 1:
        return (k + 1) ** 2
    return k * (k + 1)

T = 1
while max_dist(T) < X:
    T += 1

print(T)
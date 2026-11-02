a = [list(map(int, input().split())) for _ in range(2)]

for i in a:
    print(f"{sum(i) / 4:.1f}", end=' ')
print()

for i in range(len(a[0])):
    print(f"{(a[0][i] + a[1][i]) / 2:.1f}", end=' ')
print()

print(f"{sum(j for i in a for j in i) / 8:.1f}")
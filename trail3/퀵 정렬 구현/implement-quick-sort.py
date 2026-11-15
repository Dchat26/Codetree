import sys
import random

def quick_sort(arr, low, high):
    while low < high:
        pivot = arr[random.randint(low, high)]
        lt, i, gt = low, low, high
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        if lt - low < high - gt:
            quick_sort(arr, low, lt - 1)
            low = gt + 1
        else:
            quick_sort(arr, gt + 1, high)
            high = lt - 1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    quick_sort(arr, 0, n - 1)
    print(*arr)

main()
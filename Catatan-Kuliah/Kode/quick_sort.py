def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i


def quick_sort(a, low, high):
    if low >= high:
        return
    p = partition(a, low, high)
    quick_sort(a, low, p - 1)
    quick_sort(a, p + 1, high)

if __name__ == "__main__":
    a = [5, 3, 8, 4, 1, 3]
    quick_sort(a, 0, len(a) - 1)
    print(a)

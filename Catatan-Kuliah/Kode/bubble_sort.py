def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        changed = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                changed = True
        if not changed:
            break

if __name__ == "__main__":
    a = [5, 3, 8, 4, 1, 3]
    bubble_sort(a)
    print(a)

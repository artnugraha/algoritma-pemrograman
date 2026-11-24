def merge(a, tmp, l, m, r):
    i, j, k = l, m, l
    while i < m and j < r:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i < m:
        tmp[k] = a[i]
        i += 1
        k += 1
    while j < r:
        tmp[k] = a[j]
        j += 1
        k += 1
    a[l:r] = tmp[l:r]


def merge_sort(a, tmp, l, r):
    if r - l <= 1:
        return
    m = l + (r - l) // 2
    merge_sort(a, tmp, l, m)
    merge_sort(a, tmp, m, r)
    merge(a, tmp, l, m, r)

if __name__ == "__main__":
    a = [5, 3, 8, 4, 1, 3]
    merge_sort(a, [0.0] * len(a), 0, len(a))
    print(a)

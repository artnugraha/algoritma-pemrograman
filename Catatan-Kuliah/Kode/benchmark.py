def linear_count(a, x):
    for i, value in enumerate(a):
        if value == x:
            return i + 1
    return len(a)


def binary_count(a, x):
    low, high = 0, len(a) - 1
    count = 0
    while low <= high:
        mid = low + (high - low) // 2
        count += 1
        if a[mid] == x:
            break
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return count


if __name__ == '__main__':
    print('N,linear,binary')
    for n in (10, 100, 1000, 10000, 100000, 1000000):
        a = list(range(0, 2*n, 2))
        print(f'{n},{linear_count(a, -1)},{binary_count(a, -1)}')

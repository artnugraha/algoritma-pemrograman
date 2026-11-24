def selection_sort(a):
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]

if __name__ == "__main__":
    a = [5, 3, 8, 4, 1, 3]
    selection_sort(a)
    print(a)

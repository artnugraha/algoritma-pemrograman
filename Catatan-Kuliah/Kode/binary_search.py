def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = [2, 5, 8, 12, 16, 23, 38]
index = binary_search(data, 23)

if index != -1:
    print(f"Indeks: {index}")
else:
    print("Data tidak ditemukan.")

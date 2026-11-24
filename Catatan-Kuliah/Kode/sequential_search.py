def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


data = [10, 50, 30, 70, 80, 20]
index = sequential_search(data, 30)

if index != -1:
    print(f"Indeks: {index}")
else:
    print("Data tidak ditemukan.")

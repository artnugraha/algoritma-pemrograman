def find_element_linear(table, z):
    for i in range(len(table)):
        if table[i]["z"] == z:
            return i
    return -1


def find_element_binary(table, z):
    low, high = 0, len(table) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if table[mid]["z"] == z:
            return mid
        elif table[mid]["z"] < z:
            low = mid + 1
        else:
            high = mid - 1
    return -1


table = [
    {"z": 1, "density": 0.000089, "name": "Hidrogen"},
    {"z": 2, "density": 0.000178, "name": "Helium"},
    {"z": 6, "density": 2.26, "name": "Karbon"},
    {"z": 13, "density": 2.70, "name": "Aluminium"},
    {"z": 14, "density": 2.33, "name": "Silikon"},
    {"z": 26, "density": 7.87, "name": "Besi"},
    {"z": 29, "density": 8.96, "name": "Tembaga"},
    {"z": 79, "density": 19.32, "name": "Emas"}
]

try:
    z = int(input("Nomor atom: "))
except ValueError:
    raise SystemExit("Masukan harus berupa bilangan bulat.")
if z <= 0:
    raise SystemExit("Nomor atom harus positif.")

i = find_element_binary(table, z)
j = find_element_linear(table, z)
assert i == j

if i == -1:
    print("Unsur tidak terdapat dalam tabel parsial.")
else:
    el = table[i]
    print(f"{el['name']} (Z={el['z']}): {el['density']:.6g} g/cm^3")

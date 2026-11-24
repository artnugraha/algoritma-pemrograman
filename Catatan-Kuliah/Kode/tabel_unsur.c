#include <stdio.h>

typedef struct
{
    int z;
    double density;
    char name[20];
} Element;

int find_element_linear(const Element table[], int n, int z)
{
    for (int i = 0; i < n; i++)
        if (table[i].z == z)
            return i;
    return -1;
}

int find_element_binary(const Element table[], int n, int z)
{
    int low = 0, high = n - 1;
    while (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (table[mid].z == z)
            return mid;
        else if (table[mid].z < z)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main(void)
{
    Element table[] = {
        {1, 0.000089, "Hidrogen"},
        {2, 0.000178, "Helium"},
        {6, 2.26, "Karbon"},
        {13, 2.70, "Aluminium"},
        {14, 2.33, "Silikon"},
        {26, 7.87, "Besi"},
        {29, 8.96, "Tembaga"},
        {79, 19.32, "Emas"}
    };
    int n = sizeof(table) / sizeof(table[0]);
    int z;
    printf("Nomor atom: ");
    if (scanf("%d", &z) != 1 || z <= 0)
        return 1;

    int i = find_element_binary(table, n, z);
    int j = find_element_linear(table, n, z);
    if (i != j)
    {
        fprintf(stderr, "Hasil pencarian berbeda.\n");
        return 1;
    }
    if (i == -1)
        printf("Unsur tidak terdapat dalam tabel parsial.\n");
    else
        printf("%s (Z=%d): %.6g g/cm^3\n",
               table[i].name, table[i].z, table[i].density);
    return 0;
}

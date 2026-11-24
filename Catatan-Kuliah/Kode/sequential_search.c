#include <stdio.h>

int sequential_search(const int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            return i;
        }
    }
    return -1;
}

int main(void)
{
    int data[] = {10, 50, 30, 70, 80, 20};
    int n = sizeof(data) / sizeof(data[0]);
    int index = sequential_search(data, n, 30);

    if (index != -1)
        printf("Indeks: %d\n", index);
    else
        printf("Data tidak ditemukan.\n");

    return 0;
}

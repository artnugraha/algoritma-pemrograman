#include <stdio.h>

int binary_search(const int arr[], int n, int x)
{
    int low = 0;
    int high = n - 1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (arr[mid] == x)
            return mid;
        else if (arr[mid] < x)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main(void)
{
    int data[] = {2, 5, 8, 12, 16, 23, 38};
    int n = sizeof(data) / sizeof(data[0]);
    int index = binary_search(data, n, 23);

    if (index != -1)
        printf("Indeks: %d\n", index);
    else
        printf("Data tidak ditemukan.\n");

    return 0;
}

#include <stdio.h>

void swap(double *a, double *b)
{
    double temp = *a;
    *a = *b;
    *b = temp;
}

int partition(double a[], int low, int high)
{
    double pivot = a[high];
    int i = low;
    for (int j = low; j < high; j++) {
        if (a[j] < pivot) {
            swap(&a[i], &a[j]);
            i++;
        }
    }
    swap(&a[i], &a[high]);
    return i;
}

void quick_sort(double a[], int low, int high)
{
    if (low >= high) return;
    int p = partition(a, low, high);
    quick_sort(a, low, p - 1);
    quick_sort(a, p + 1, high);
}

int main(void)
{
    double a[] = {5, 3, 8, 4, 1, 3};
    int n = sizeof(a) / sizeof(a[0]);
    quick_sort(a, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%g ", a[i]);
    puts("");
    return 0;
}

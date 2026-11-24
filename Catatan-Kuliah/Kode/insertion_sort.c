#include <stdio.h>

void insertion_sort(double a[], int n)
{
    for (int i = 1; i < n; i++) {
        double key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

int main(void)
{
    double a[] = {5, 3, 8, 4, 1, 3};
    int n = sizeof(a) / sizeof(a[0]);
    insertion_sort(a, n);
    for (int i = 0; i < n; i++) printf("%g ", a[i]);
    puts("");
    return 0;
}

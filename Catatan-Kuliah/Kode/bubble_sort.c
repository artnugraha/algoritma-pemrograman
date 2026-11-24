#include <stdio.h>

void swap(double *a, double *b)
{
    double temp = *a;
    *a = *b;
    *b = temp;
}

void bubble_sort(double a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        int changed = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(&a[j], &a[j + 1]);
                changed = 1;
            }
        }
        if (!changed) break;
    }
}

int main(void)
{
    double a[] = {5, 3, 8, 4, 1, 3};
    int n = sizeof(a) / sizeof(a[0]);
    bubble_sort(a, n);
    for (int i = 0; i < n; i++) printf("%g ", a[i]);
    puts("");
    return 0;
}

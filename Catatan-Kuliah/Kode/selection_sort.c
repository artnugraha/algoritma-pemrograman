#include <stdio.h>

void swap(double *a, double *b)
{
    double temp = *a;
    *a = *b;
    *b = temp;
}

void selection_sort(double a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[m]) m = j;
        }
        if (m != i) swap(&a[i], &a[m]);
    }
}

int main(void)
{
    double a[] = {5, 3, 8, 4, 1, 3};
    int n = sizeof(a) / sizeof(a[0]);
    selection_sort(a, n);
    for (int i = 0; i < n; i++) printf("%g ", a[i]);
    puts("");
    return 0;
}

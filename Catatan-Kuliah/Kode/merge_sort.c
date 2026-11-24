#include <stdio.h>

void merge(double a[], double tmp[], int l, int m, int r)
{
    int i = l, j = m, k = l;
    while (i < m && j < r) {
        if (a[i] <= a[j]) tmp[k++] = a[i++];
        else tmp[k++] = a[j++];
    }
    while (i < m) tmp[k++] = a[i++];
    while (j < r) tmp[k++] = a[j++];
    for (k = l; k < r; k++) a[k] = tmp[k];
}

void merge_sort(double a[], double tmp[], int l, int r)
{
    if (r - l <= 1) return;
    int m = l + (r - l) / 2;
    merge_sort(a, tmp, l, m);
    merge_sort(a, tmp, m, r);
    merge(a, tmp, l, m, r);
}

int main(void)
{
    double a[] = {5, 3, 8, 4, 1, 3};
    int n = sizeof(a) / sizeof(a[0]);
    double tmp[sizeof(a) / sizeof(a[0])];
    merge_sort(a, tmp, 0, n);
    for (int i = 0; i < n; i++) printf("%g ", a[i]);
    puts("");
    return 0;
}

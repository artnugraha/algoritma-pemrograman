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
    double e[] = {4.5, 2.1, 0.5, 9.8, 1.2};
    int n = sizeof(e) / sizeof(e[0]);
    insertion_sort(e, n);
    double median = (n % 2 != 0) ? e[n / 2]
        : (e[n / 2 - 1] + e[n / 2]) / 2.0;
    printf("Min = %.2f J\n", e[0]);
    printf("Median = %.2f J\n", median);
    printf("Max = %.2f J\n", e[n - 1]);
    return 0;
}

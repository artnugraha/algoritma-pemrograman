#include <stdio.h>

int linear_count(const int a[], int n, int x)
{
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i + 1;
    return n;
}

int binary_count(const int a[], int n, int x)
{
    int low = 0, high = n - 1, count = 0;
    while (low <= high)
    {
        int mid = low + (high - low) / 2;
        count++;
        if (a[mid] == x) break;
        if (a[mid] < x) low = mid + 1;
        else high = mid - 1;
    }
    return count;
}

int main(void)
{
    static int a[1000000];
    puts("N,linear,binary");
    for (int n = 10; n <= 1000000; n *= 10)
    {
        for (int i = 0; i < n; i++) a[i] = 2*i;
        printf("%d,%d,%d\n", n, linear_count(a,n,-1), binary_count(a,n,-1));
    }
    return 0;
}

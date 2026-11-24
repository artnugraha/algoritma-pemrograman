#include <math.h>

int find_near(const double data[], int n, double target, double eps)
{
    for (int i = 0; i < n; i++)
        if (fabs(data[i] - target) <= eps)
            return i;
    return -1;
}

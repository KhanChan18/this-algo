#include <stdio.h>

int main(void) {
    int n, step = 0;
    scanf("%d", &n);
    while (n != 1) {
        if (n % 2 == 0)
            n = n / 2;
        else
            n = (3 * n + 1) / 2;
        step = step + 1;
    }
    printf("%d\n", step);
    return 0;
}
#include <stdio.h>

int ans[30] = {0};

int main() {
    int num1, num2, dig;
    while (scanf("%d%d%d", &num1, &num2, &dig) != EOF) {
        int n = 0;
        int sum = num1 + num2;

        ans[n] = sum % dig;
        sum = sum / dig;

        while (sum != 0) {
            n = n + 1;
            ans[n] = sum % dig;
            sum = sum / dig;
        }

        for (int i = n; i >= 0; i--) {
            printf("%d", ans[i]);
        }
        printf("\n");
    }
}

#include <stdio.h>

#define MAX_LEN 210

int arr[MAX_LEN];

int main() {
    int n, x;
    while (scanf("%d", &n) != EOF) {
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
        }
    
    scanf("%d", &x);
    int k;
    for (k = 0; k < n; k++) {
        if (arr[k] == x) {
            printf("%d\n", k);
            break;
        }
    }

    if (k == n) printf("-1\n");
    }
    
    return 0;
}

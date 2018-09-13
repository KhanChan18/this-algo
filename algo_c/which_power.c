#include <stdio.h>

#define MAX_LEN 100000
//int school[MAX_LEN] = {0};

int main(void) {
    // const int MAX_LEN = 100000;
    int school[MAX_LEN] = {0};
    int n, schid, score;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &schid, &score);
        school[schid] += score;
    }

    int k = 0, MAX = -1;
    for (int i = 0; i < n; i++) {
        if (school[i] > MAX) {
            MAX = school[i];
            k = i;
        }
    }

    printf("%d %d\n", k, MAX);
    return 0;
}

#include <stdio.h>

int calen[13][2] = {
    {0, 0},   {31, 31}, {28, 29},
    {31, 31}, {30, 30}, {31, 31},
    {30, 30}, {31, 31}, {31, 31},
    {30, 30}, {31, 31}, {30, 30},
    {31, 31}
};

int isLeap(int year) {
    int period_4 = (year % 4 == 0);
    int period_100 = (year % 100 != 0);
    int period_400 = (year % 400 == 0);
    return (period_4 && period_100) || period_400;
}

int main(void) {
    int time1, y1, m1, d1;
    int time2, y2, m2, d2;

    while (scanf("%d%d", &time1, &time2) != EOF) {
        // Make sure time2 is always latter than time1
        // Swap them if necessary.
        if (time1 > time2) {
            int temp = time1;
            time1 = time2;
            time2 = temp;
        }

        y1 = time1 / 10000;
        y2 = time2 / 10000;
        m1 = time1 % 10000 / 100;
        m2 = time2 % 10000 / 100;
        d1 = time1 % 100;
        d2 = time2 % 100;

        int ans = 1;
        for (; y1 < y2 || m1 < m2 || d1 < d2; ans++) {
            d1 = d1 + 1;
            if (d1 == calen[m1][isLeap(y1)] + 1) {
                m1 = m1 + 1;
                d1 = 1;
            }

            if (m1 == 13) {
                y1 = y1 + 1;
                m1 = 1;
            }
        }

        printf("%d\n", ans);
    }
    return 0;
}

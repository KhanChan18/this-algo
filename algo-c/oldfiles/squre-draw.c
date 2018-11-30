#include <stdio.h>

int main() {
    int col, row;
    char c;

    scanf("%d %c", &col, &c);
    row = (col % 2 == 1)?(col / 2 + 1):(col / 2);

    // Line 0
    for (int i = 0; i < col; i++) {
        printf("%c", c);
    }
    printf("\n");

    // Line in the middles
    for (int i = 0; i < row - 2; i++) {
        printf("%c", c);
        for (int j = 0; j < col - 2; j++) {
            printf(" ");
        }
        printf("%c\n", c);
    }

    // Line COL - 1
    for (int i = 0; i < col; i++) {
        printf("%c", c);
    }
    printf("\n");

    return 0;
}

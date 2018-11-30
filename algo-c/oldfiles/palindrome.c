#include <stdio.h>
#include <string.h>

#define MAX_LEN 255

int is_palindrome(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        if (str[i] != str[len - i - 1])
            return 0;
    }
    return 1;
}

int main(void) {
    char str[MAX_LEN];
    while (gets(str)) {
        int flag = is_palindrome(str);
        if (flag)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

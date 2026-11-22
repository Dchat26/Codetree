#include <stdio.h>

int main() {
    int a, b;

    a = 5;
    b = 3;
    a = b;

    printf("%d\n%d", a, b);

    return 0;
}
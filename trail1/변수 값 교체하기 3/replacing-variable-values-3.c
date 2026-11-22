#include <stdio.h>

int main() {
    int a, b, temp;

    a = 3;
    b = 5;

    temp = a;
    a = b;
    b = temp;

    printf("%d\n%d", a, b);

    return 0;
}
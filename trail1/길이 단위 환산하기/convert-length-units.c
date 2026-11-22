#include <stdio.h>

int main() {
    double a, b;

    a = 30.48;

    scanf("%lf", &b);
    printf("%.1lf", a * b);

    return 0;
}
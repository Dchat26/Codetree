#include <stdio.h>

int main() {
    int a;
    double b, c;

    a = 13;
    b = 0.165;
    c = a * b;

    printf("%d * %.6lf = %.6lf", a, b, c);

    return 0;
}
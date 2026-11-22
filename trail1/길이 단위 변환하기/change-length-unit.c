#include <stdio.h>

int main() {
    double a, b;
    
    a = 30.48;
    b = 160934;

    printf("9.2ft = %.1lfcm\n", a * 9.2);
    printf("1.3mi = %.1lfcm", b * 1.3);

    return 0;
}
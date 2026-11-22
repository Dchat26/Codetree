#include <stdio.h>

int main() {
    int a;

    scanf("%d", &a);
    printf("%s", a == 100 ? "pass" : "failure");

    return 0;
}
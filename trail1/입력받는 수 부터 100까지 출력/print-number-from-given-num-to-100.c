#include <stdio.h>

int main() {
    int a;

    scanf("%d", &a);
    
    for (int i = a; i <= 100; i++) {
        printf("%d ", i);
    }

    return 0;
}
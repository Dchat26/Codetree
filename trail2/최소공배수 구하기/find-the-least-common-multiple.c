#include <stdio.h>


int lcm(int a, int b, int c) {
    return a * b / c;
}


int gcd(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }

    return a;
}


int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    
    printf("%d", lcm(n, m, gcd(n, m)));
    
    return 0;
}
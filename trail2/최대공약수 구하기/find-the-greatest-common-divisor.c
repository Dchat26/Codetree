#include <stdio.h>
#include <stdbool.h>


int F(int a, int b) {
    int prod = 1;
    int val;
    while (1) {
        if (a >= b) val = b;
        else val = a;

        bool is_TF = true;
        for (int i = val; i >= 2; i--) {
            if (a % i == 0 && b % i == 0) {
                prod *= i;

                a /= i;
                b /= i;

                is_TF = false;
                break;
            }
        }

        if (is_TF) break;
    }

    return prod;
}


int main() {
    int n, m, answer;

    scanf("%d %d", &n, &m);

    answer = F(n, m);
    printf("%d", answer);
    
    return 0;
}
#include <stdio.h>


void F(int a) {
    int val = 1;
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            printf("%d ", val);
            val++;

            if (val == 10) val = 1;
        }
        printf("\n");
    }
}


int main() {
    int N;
    scanf("%d", &N);
    
    F(N);

    return 0;
}
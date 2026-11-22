#include <stdio.h>

int main() {
    int h, w, s;

    scanf("%d %d", &h, &w);

    s = (10000 * w) / (h * h);
    if (s >= 25) {
        printf("%d\nObesity", s);
    }
    else {
        printf("%d", s);
    }

    return 0;
}
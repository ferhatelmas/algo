#include <stdio.h>

int main() {
    int t, a, b;
    scanf("%d\n", &t);
    while (t--) {
        scanf("%d %d\n", &a, &b);
        if (a > b) printf(">\n");
        else if (a < b) printf("<\n");
        else printf("=\n");
    }
    return 0;
}

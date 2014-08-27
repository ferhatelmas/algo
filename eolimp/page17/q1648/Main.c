#include <stdio.h>

// Java is too slow for this problem
int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n & -n);
    return 0;
}

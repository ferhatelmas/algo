#include <stdio.h>
#include <limits.h>

// Java is too slow for this problem
int main() {
    int i, j;
    scanf("%d %d", &i, &j);
    printf("%d\n", i & (INT_MAX << j));
    return 0;
}

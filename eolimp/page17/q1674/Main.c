#include <stdio.h>
#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b

// There is a weird bug on the judge
// throws runtime in java
int main() {
    int a, b, c, t, n;
    scanf("%d %d %d\n%d", &a, &b, &c, &n);
    while(n-- > 0) {
        scanf("%d", &t);
        c = t < 0 ? max(c + t, a) : min(c + t, b);
    }
    printf("%d\n", c);
    return 0;
}

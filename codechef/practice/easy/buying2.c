#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while(t-- > 0) {
        int n, k;
        scanf("%d %d", &n, &k);
        int s = 0, m, min = 101;
        while(n-- > 0) {
            scanf("%d", &m);
            s += m;
            if (m < min) {
                min = m;
            }
        }

        printf("%d\n", s % k >= min ? -1 : s / k);
    }
}

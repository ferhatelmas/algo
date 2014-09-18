#include <cstdio>
#include <cstring>

int ns[101];

int main() {
    int n, c;
    while(true) {
        memset(ns, 0, 101 * sizeof(int));
        scanf("%d", &n);
        if(n == 0) break;
        while(n-- > 0) {
            scanf("%d", &c);
            ns[c]++;
        }

        bool f = false;
        for(int i=1; i<101; i++) {
            for(int j=0; j<ns[i]; j++) {
                if(!f) {
                    printf("%d", i);
                    f = !f;
                } else {
                    printf(" %d", i);
                }
            }
        }
        printf("\n");
    }
    return 0;
}

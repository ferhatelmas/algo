#include <cstdio>

int ns[101] = {};

int main() {
    int n, k;
    scanf("%d", &n);
    while(n-- > 0) {
        scanf("%d", &k);
        ns[k]++;
    }

    bool f = false;
    for(int i=1; i<101; i++)
        for(int j=ns[i]; j>0; j--)
            if(f)
                printf(" %d", i);
            else {
                f = !f;
                printf("%d", i);
            }
    printf("\n");
}

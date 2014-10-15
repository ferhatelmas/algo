#include <cstdio>

using namespace std;

int main() {
    int n, t, ns[10001] = {0};
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d", &t);
        ns[t]++;
    }

    bool b = false;
    for(int i=0; i<10001; i++) {
        while(ns[i]-- > 0) {
            if(!b) {
                printf("%d", i);
                b = !b;
            } else {
                printf(" %d", i);
            }
        }
    }
    printf("\n");
}

#include <cstdio>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    long long **ns = new long long*[n];
    for(int i=0; i<n; i++)
        ns[i] = new long long[m];
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            long long l;
            scanf("%lld", &l);
            if(i == 0 && j == 0) ns[i][j] = l;
            else if(i == 0) ns[i][j] = l + ns[i][j-1];
            else ns[i][j] = ns[i-1][j] + (j > 0 ? ns[i][j-1] - ns[i-1][j-1] : 0) + l;
        }
    }

    int t;
    scanf("%d", &t);
    while(t-- > 0) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        printf("%lld\n",
            ns[c-1][d-1] -
            (b > 1 ? ns[c-1][b-2] : 0) -
            (a > 1 ? ns[a-2][d-1] : 0) +
            (a > 1 && b > 1 ? ns[a-2][b-2] : 0));
    }
    return 0;
}

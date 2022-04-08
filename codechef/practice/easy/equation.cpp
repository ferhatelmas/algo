#include <stdio.h>

#define min(x, y) ((x) < (y) ? (x) : (y))

int main() {
  int t, n, a, b, c, i, j, k;
  long long sum;
  scanf("%d", &t);
  while(t--) {
    scanf("%d %d %d %d", &n, &a, &b, &c);
    sum = 0;
    for(i=0; i<=a; i++) {
      k = min(n-i, b);
      for(j=0; j<=k; j++) {
        sum += min(n-i-j, c) + 1;
      }
    }
    printf("%lld\n", sum);
  }
}
#include <stdio.h>

int main() {
  int N, n, i, cnt, mul;
  while(scanf("%d", &n), n) {
    mul = 1, i = 2, N = n;
    while(i <= n) {
      cnt = 0;
      while(n%i == 0) {
        cnt++;
        n /= i;
      }
      mul *= (2*cnt+1);
      if(++i > 45000) {
        mul *= 3;
        break;
      }
    }
    printf("%d %d\n", N, mul/2+1);
  }
  return 0;
}
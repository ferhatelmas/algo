#include <stdio.h>

int main() {
  int n, r = 0, k;
  scanf("%d", &n);
  while (n-- > 0) {
    scanf("%d", &k);
    r ^= k;
  }
  printf("%d\n", r);
  return 0;
}

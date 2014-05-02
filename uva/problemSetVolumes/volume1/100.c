#include <stdio.h>

int cycle(int m) {
  int i = 1;
  while(m != 1) {
    if(m%2 == 0) m /= 2;
    else m = 3*m+1;
    i++;
  }
  return i;
}

int main() {
  int m, n, mo, no, i, max, temp;
  while(scanf("%d %d\n", &m, &n) == 2) {
    mo = m; no = n;

    if(m > n) {
      int temp = m;
      m = n;
      n = temp;
    }

    max = cycle(m);
    for(i=m+1; i<=n; i++) {
      temp = cycle(i);
      if(temp > max) max = temp;
    }
    printf("%d %d %d\n", mo, no, max);
  }
  return 0;
}
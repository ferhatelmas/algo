#include <stdio.h>

#define max(x, y) ((x) > (y) ? (x) : (y))

int c[1000][1000];
char b[1000][1000];

int main() {
  int i, j, k, t, n;
  scanf("%d", &t);
  while(t--) {
    scanf("%d\n", &n);
    for(i=-1; ++i^n;) gets(b[i]);

    for(j=n; j--;) {
      for(i=0; i^n; i++) {
        k = 0;
        if((j+1) < n && (i-2) >= 0) k = max(k, c[i-2][j+1]);
        if((j+2) < n && (i-1) >= 0) k = max(k, c[i-1][j+2]);
        if((j+2) < n && (i+1) < n) k = max(k, c[i+1][j+2]);
        if((j+1) < n && (i+2) < n) k = max(k, c[i+2][j+1]);

        if(b[i][j] == 'K') {
          printf("%d\n", k);
          break;
        }
        c[i][j] = k + (b[i][j] == 'P');
      }
      if(i < n) break;
    }
  }
}
#include <stdio.h>
#include <algorithm>

int main() {
  int n;
  while(scanf("%d", &n), n != 0) {
    int p[n];
    for(int i=0; i<n; i++) 
      scanf("%d", &p[i]);

    std::sort(p, p + n);
    int cnt = 0;
    for(int i=n-1; i>=2; i--) {
      int b = 0, e = i-1;
      while(b < e) {
        if(p[i] > p[e] + p[b]) {
          cnt += e - b;
          b++;
        } else e--;
      }
    }
    printf("%d\n", cnt);
  }
}
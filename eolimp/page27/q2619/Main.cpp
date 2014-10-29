#include <cstdio>

int main() {
  int n, ns[1000000], sum1 = 0, sum2 = 0;
  scanf("%d", &n);
  for(int i=0; i<n; i++) {
    scanf("%d", &ns[i]);
    sum1 += ns[i];
  }

  if(sum1%2 == 0) {
    for(int i=0; i<n; i++) {
      sum1 -= ns[i];
      sum2 += ns[i];
      if(sum1 == sum2) {
        printf("%d\n", i+1);
        break;
      } else if(sum1 < sum2) {
        printf("%d\n", -1);
        break;
      }
    }
  } else 
    printf("%d\n", -1);
}

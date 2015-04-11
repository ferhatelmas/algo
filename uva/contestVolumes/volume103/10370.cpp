#include <cstdio>

using namespace std;

int buf[1000];

int main() {
  int t, n;
  scanf("%d", &t);
  while (t-- > 0) {
    scanf("%d", &n);
    double sum = 0;
    for (int i = 0; i < n; i++) {
      scanf("%d", &buf[i]);
      sum += buf[i];
    }
    sum /= n;
    int c = 0;
    for (int i = 0; i < n; i++) {
      if (buf[i] > sum) c++;
    }
    printf("%.3f%%\n", (c * 100.0) / n);
  }
}

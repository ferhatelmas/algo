#include <cstring>
#include <iostream>

using namespace std;

bool c[3000];

int main() {
  int n;
  while (cin >> n) {
    memset(c, false,  3000 * sizeof(bool));
    bool jolly = true;
    int p = -1, r, i = 0;
    for (; i < n; i++) {
      cin >> r;
      if (i > 0) {
        int t = abs(p - r);
        if (t >= n || t < 1 || c[t]) {
          jolly = false;
          break;
        }
        c[t] = true;
      }
      p = r;
    }
    while (++i < n) cin >> r;
    cout << (jolly ? "Jolly" : "Not jolly") << endl;
  }
}


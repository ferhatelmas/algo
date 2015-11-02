#include <iostream>

using namespace std;

int count(int i) {
  i = i - ((i >> 1) & 0x55555555);
  i = (i & 0x33333333) + ((i >> 2) & 0x33333333);
  return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

int main() {
  int k, c = 0, v = 0;
  cin >> k;
  while (k-- > 0) {
    int t, n;
    cin >> t;
    n = count(t);
    if (n > c) {
      c = n;
      v = t;
    } else if (n == c && t < v) {
      v = t;
    }
  }
  cout << v << endl;
}

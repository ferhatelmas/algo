#include <iostream>

using namespace std;

int c[10000];

int main() {
  int n = 0, t, j;
  while (cin >> t) {
    j = n;
    while (j > 0 && t < c[j-1]) {
      c[j] = c[j-1];
      j--;
    }
    c[j] = t;
    n++;
    cout << (n%2 == 0 ? (c[n/2] + c[n/2-1])/2 : c[n/2]) << endl;
  }
}

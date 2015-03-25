#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int main() {
  int t, c, r, i = 1;
  cin >> t;
  while (t-- > 0) {
    cin >> c >> r;
    if (c == r) {
      cout << "Case #" << i << ": " << 0 << endl;
    } else {
      set<int> s;
      c -= r;
      cout << "Case #" << i << ":";
      for (int i = 1; i <= sqrt(c); i++) {
        if (c % i == 0) {
          if (i > r) s.insert(i);
          if (c / i > r) s.insert(c / i);
        }
      }
      for (auto it = s.begin(); it != s.end(); it++) {
        cout << " " << *it;
      }
      cout << endl;
    }
    i++;
  }
}

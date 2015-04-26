#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
  int t, n, p;
  cin >> t;
  while (t-- > 0) {
    cin >> n >> p;
    unordered_set<int> s;
    while (p-- > 0) {
      int k;
      cin >> k;
      for (int i = 0; i <= n; i += k) {
        int m = i % 7;
        if (m != 0 && m != 6) {
          s.insert(i);
        }
      }
    }
    cout << s.size() << endl;
  }
}

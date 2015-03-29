#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int t, n;
  vector<int> v;
  cin >> t;
  while (t-- > 0) {
    while(cin >> n && n != 0) {
      v.push_back(n);
    }
    sort(v.begin(), v.end(), greater<int>());
    int s = 0, k = 1;
    for (auto it = v.begin(); it != v.end(); it++) {
      s += 2 * pow(*it, k++);
      if (s > 5000000) break;
    }
    cout << (s > 5000000 ? "Too expensive" : to_string(s)) << endl;
    v.clear();
  }
}

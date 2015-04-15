#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

using namespace std;

int sum(vector<int>& v, int k, int n) {
  int s = 0, c = v[k];
  for (int i = 0; i < n; i++) {
    if (i != k) {
      s += abs(v[i] - c);
    }
  }
  return s;
}

int main() {
  int t;
  cin >> t;
  while (t-- > 0) {
    int n, r, a = 30000, b = 0;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
      cin >> r;
      v.push_back(r);
    }
    sort(v.begin(), v.end());

    if (n % 2 == 0) {
      cout << min(sum(v, n / 2, n), sum(v, n / 2 - 1, n)) << endl;
    } else {
      cout << sum(v, n / 2, n) << endl;
    }
  }
}

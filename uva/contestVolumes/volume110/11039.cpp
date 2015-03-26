#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool cmp(int i, int j) { return abs(i) > abs(j); }

int main() {
  int t, n, p;
  cin >> t;
  while (t-- > 0) {
    cin >> n;
    vector<int> v;
    while (n-- > 0) {
      cin >> p;
      v.push_back(p);
    }

    sort(v.begin(), v.end(), cmp);
    int k = 0, p = 0;
    for (auto it = v.begin(); it != v.end(); it++) {
      if (it == v.begin()) k++;
      else if ((*it > 0 && p < 0) || (*it < 0 && p > 0)) k++;
      p = *it;
    }
    cout << k << endl;
  }
}

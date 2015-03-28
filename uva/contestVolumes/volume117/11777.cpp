#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int t, i = 1, n;
  cin >> t;
  while (t-- > 0) {
    double s = 0;
    for (int j = 0; j < 4; j++) {
      cin >> n;
      s += n;
    }
    vector<int> v;
    for (int j = 0; j < 3; j++) {
      cin >> n;
      v.push_back(n);
    }
    sort(v.begin(), v.end());
    s += (v[1] + v[2]) / 2;

    cout << "Case " << i++ << ": ";
    if (s >= 90) {
      cout << "A";
    } else if (s >= 80) {
      cout << "B";
    } else if (s >= 70) {
      cout << "C";
    } else if (s >= 60) {
      cout << "D";
    } else {
      cout << "F";
    }
    cout << endl;
  }
}

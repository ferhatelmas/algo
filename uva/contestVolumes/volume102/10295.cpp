#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  int t, n, v;
  string s;
  cin >> t >> n;

  unordered_map<string, int> m;
  while (t-- > 0) {
    cin >> s >> v;
    m[s] = v;
  }

  t = 0;
  while (cin >> s) {
    if (s == ".") {
      cout << t << endl;
      t = 0;
    } else {
      auto it = m.find(s);
      if (it != m.end()) t += m[s];
    }
  }
}

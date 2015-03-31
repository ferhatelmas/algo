#include <iomanip>
#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

int main() {
  int t;
  bool first = false;
  string s;
  cin >> t;
  getline(cin, s);
  getline(cin, s);
  cout << setprecision(4);
  while (t-- > 0) {
    map<string, int> m;
    int k = 0;
    while (getline(cin, s) && !s.empty()) {
      m[s]++;
      k++;
    }
    if (first) {
      cout << endl;
    }
    first = true;
    for (auto it = m.begin(); it != m.end(); it++) {
      printf("%s %.4f\n", it->first.c_str(), it->second * 100.0 / k);
    }
  }
}

#include <iostream>

using namespace std;

int main() {
  string s1, s2;

  while (cin >> s1 >> s2 && !(s1 == "0" && s2 == "0")) {
    int l1 = s1.size(), l2 = s2.size(), c = 0, p = 0;
    for (int i = 0, m = max(l1, l2); i<m; i++) {
      p += (i >= l1 ? 0 : (s1[l1-i-1] - '0'));
      p += (i >= l2 ? 0 : (s2[l2-i-1] - '0'));
      if (p > 9) {
        c++;
        p = 1;
      } else {
        p = 0;
      }
    }
    cout << (c == 0 ? "No" : to_string(c));
    cout << " carry operation" << (c > 1 ? "s." : ".") << endl;
  }
}

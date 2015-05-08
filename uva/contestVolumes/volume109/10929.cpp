#include <iostream>

using namespace std;

int main() {
  string s;
  int n;
  while (cin >> s && s != "0") {
    n = 0;
    for (int i = 0, k = s.size(); i < k; i++) {
      n += (s[i] - '0') * (i % 2 ? 1 : -1);
    }
    cout << s << " is " << (n % 11 == 0 ? "" : "not ") << "a multiple of 11." << endl;
  }
}

#include <iostream>
#include <string>

using namespace std;

int main() {
  unsigned int t, n;
  cin >> t;
  while (t-- > 0) {
    cin >> n;
    int i = 0;
    string s = to_string(n), p = string(s.rbegin(), s.rend());
    while (i < 1000 && s != p && n < 4294967296) {
      n = stoul(s) + stoul(p);
      s = to_string(n);
      p = string(s.rbegin(), s.rend());
      i++;
    }
    cout << i << " " << n << endl;
  }
}

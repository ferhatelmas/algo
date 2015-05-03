#include <bitset>
#include <iostream>

using namespace std;

int main() {
  int n;
  while (cin >> n && n > 0) {
    bitset<32> b(n);
    cout << "The parity of ";
    bool first = false;
    string s = b.to_string();
    auto i = s.begin();
    while (i != s.end()) {
      if (*i == '1') {
        cout << *i;
        first = true;
      } else if (first) {
        cout << *i;
      }
      i++;
    }
    cout << " is " << b.count() << " (mod 2)."<< endl;
  }
}

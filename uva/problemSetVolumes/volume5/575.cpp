#include <iostream>

using namespace std;

int convert(string& s) {
  int p = 2, sum = 0;
  for (auto it = s.rbegin(); it != s.rend(); it++) {
    sum += (*it - '0') * (p - 1);
    p *= 2;
  }
  return sum;
}

int main() {
  string s;
  while (cin >> s && s != "0") {
    cout << convert(s) << endl;
  }
}

#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>

using namespace std;

int main() {
  string s;
  unordered_map<string, string> m;
  while (getline(cin, s) && !s.empty()) {
    auto i = s.find(" ");
    m[s.substr(i+1)] = s.substr(0, i);
  }

  while (getline(cin, s)) {
    auto it = m.find(s);
    if (it == m.end()) {
      cout << "eh" << endl;
    } else {
      cout << it->second << endl;
    }
  }
}

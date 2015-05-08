#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  string s;
  unordered_map<char, string> m;
  m['B'] = m['F'] = m['P'] = m['V'] = "1";
  m['C'] = m['G'] = m['J'] = m['K'] = m['Q'] = m['S'] = m['X'] = m['Z'] = "2";
  m['D'] = m['T'] = "3";
  m['L'] = "4";
  m['M'] = m['N'] = "5";
  m['R'] = "6";
  m['A'] = m['E'] = m['I'] = m['O'] = m['U'] = m['H'] = m['W'] = m['Y'] = "";
  while (cin >> s) {
    for (int i = 0, k = s.size(); i < k; i++) {
      if (i == 0 || m[s[i]] != m[s[i-1]]) {
        cout << m[s[i]];
      }
    }
    cout <<endl;
  }
}

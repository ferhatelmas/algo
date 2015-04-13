#include <algorithm>
#include <iostream>
#include <map>
#include <unordered_map>

using namespace std;

int main() {
  int n;
  string s;
  unordered_map<char, int> m;
  cin >> n;
  getline(cin, s);
  while (n-- > 0) {
    getline(cin, s);
    for (auto it = s.begin(); it != s.end(); it++) {
      char c = *it;
      if (c >= 'a' && c <= 'z') {
        m[c - 'a' + 'A']++;
      } else if (c >= 'A' && c <= 'Z') {
        m[c]++;
      }
    }
  }

  map<int, vector<char>*> mm;
  for (auto it = m.begin(); it != m.end(); it++) {
    if (mm.find(it->second) == mm.end()) {
      mm[it->second] = new vector<char>();
    }
    mm[it->second]->push_back(it->first);
  }

  for (auto it = mm.rbegin(); it != mm.rend(); it++) {
    vector<char>* v = it->second;
    sort(v->begin(), v->end());
    for (auto it2 = v->begin(); it2 != v->end(); it2++) {
      cout << *it2 << " " << it->first << endl;
    }
  }
}

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    int n;
    string s;
    map<string, int> m;
    cin >> n;
    getline(cin, s);
    while(n-- > 0) {
        getline(cin, s);
        m[s.substr(0, s.find(' '))]++;
    }

    for(auto& it : m)
        cout << it.first << " " << it.second << endl;
}

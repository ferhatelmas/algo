#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    string s, w;
    while(getline(cin, s)) {
        istringstream ss(s);
        bool f = false;
        while(ss >> w) {
            reverse(w.begin(), w.end());
            if(!f) {
                cout << w;
                f = !f;
            } else
                cout << " " << w;
        }
        cout << endl;
    }
}

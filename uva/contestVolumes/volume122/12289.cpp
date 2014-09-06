#include <iostream>

using namespace std;

int main() {
    int n;
    string s, one{"one"};
    cin >> n;
    while(n-- > 0) {
        cin >> s;
        if(s.length() == 5) cout << 3 << endl;
        else {
            int i = 0, c = 0;
            for(; i<3; i++) c += s[i] == one[i];
            cout << (c < 2 ? 2 : 1) << endl;
        }
    }
}

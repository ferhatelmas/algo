#include <cctype>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

int c[52];

int main() {
    string s;
    while(getline(cin, s)) {
        memset(c, 0, sizeof c);
        int m = 0;
        for(int i=0; i<s.size(); i++) {
            if(isupper(s[i])) m = max(m, ++c[s[i] - 'A']);
            else if(islower(s[i])) m = max(m, ++c[s[i] - 'a' + 26]);
        }

        for(int i=0; i<52; i++) if(c[i] == m) cout << char(i%26 + (i > 25 ? 'a' : 'A'));
        cout << " " << m << endl;
    }
}

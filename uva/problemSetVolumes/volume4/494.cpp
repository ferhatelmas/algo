#include <cctype>
#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    while(getline(cin, s)) {
        int l = s.size(), k = 0;
        for(int i=0; i<l; i++) {
            if(isalpha(s[i])) {
                k++;
                for(i++; isalpha(s[i]) && i < l; i++);
            }
        }
        cout << k << endl;
    }
}

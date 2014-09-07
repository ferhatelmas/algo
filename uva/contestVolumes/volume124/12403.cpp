#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    long res = 0, x;
    while(n-- > 0) {
        cin >> s;
        if(s == "donate") {
            cin >> x;
            res += x;
        } else
            cout << res << endl;
    }
}

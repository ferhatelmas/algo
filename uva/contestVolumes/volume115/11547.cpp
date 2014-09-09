#include <iostream>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    while(t-- > 0) {
        cin >> n;
        n = 315 * n + 36962;
        n = (n%100 - n%10) / 10;
        cout << (n >= 0 ? n : -n) << endl;
    }
}

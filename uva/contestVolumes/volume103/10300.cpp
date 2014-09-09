#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t-- > 0) {
        int n;
        cin >> n;
        long sum = 0, i, j, k;
        while(n-- > 0) {
            cin >> i >> j >> k;
            sum += i * k;
        }
        cout << sum << endl;
    }
}

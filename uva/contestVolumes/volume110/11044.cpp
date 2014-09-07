#include <cmath>
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    long a, b;
    while(n-- > 0) {
        cin >> a >> b;
        cout << (int)(ceil((a-2.0) / 3) * ceil((b-2.0) / 3)) << endl;
    }
}

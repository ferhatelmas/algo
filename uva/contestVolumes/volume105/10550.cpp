#include <iostream>

using namespace std;

int unlock(int a, int b, int c, int d) {
    int r = 1080;
    r += 9 * ((a-b+40) % 40);
    r += 9 * ((c-b+40) % 40);
    r += 9 * ((c-d+40) % 40);
    return r;
}

int main() {
    int a, b, c, d;
    while(cin >> a >> b >> c >> d) {
        if(a == b && b == c && c == d && d == 0) break;
        cout << unlock(a, b, c, d) << endl;
    }
    return 0;
}

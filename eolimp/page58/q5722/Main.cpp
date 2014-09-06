#include <iostream>
#include <set>

using namespace std;

typedef unsigned long long ull;

int main() {
    int n = 0, c = 0;
    ull r = 1;

    set<ull> s;
    while(n++ < 64) {
        s.insert(r);
        r *= 2;
    }

    cin >> n;
    while(n-- > 0) {
        cin >> r;
        c += s.count(r);
    }
    cout << c << endl;
}

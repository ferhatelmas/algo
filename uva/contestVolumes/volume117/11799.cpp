#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int n, t;
    cin >> n;
    string s;
    getline(cin, s);
    for(int i=1, m; i<=n; i++) {
        m = 0;
        getline(cin, s);
        istringstream is {s};
        while(is >> t) m = max(m, t);
        cout << "Case " << i << ": " << m << endl;
    }
}

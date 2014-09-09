#include <iostream>

using namespace std;

int main() {
    int k;
    while(cin >> k && k > 0) {
        int n, m;
        cin >> n >> m;
        while(k-- > 0) {
            int x, y;
            cin >> x >> y;
            if(x == n || y == m) cout << "divisa" << endl;
            else if(x < n && y > m) cout << "NO" << endl;
            else if(x > n && y > m) cout << "NE" << endl;
            else if(x > n && y < m) cout << "SE" << endl;
            else cout << "SO" << endl;
        }
    }
}

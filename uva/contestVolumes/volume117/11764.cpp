#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i=1; i<=t; i++) {
        int n, h = 0, l = 0, p, c;
        cin >> n;
        if(n > 1) {
            cin >> p;
            for(int j=1; j<n; j++) {
                cin >> c;
                if(c > p) h++;
                if(c < p) l++;
                p = c;
            }
        } else cin >> p;

        cout << "Case " << i << ": " << h << " " << l << endl;
    }
}

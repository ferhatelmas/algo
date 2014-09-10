#include <iostream>

using namespace std;

int main() {
    int n, b, h, w;
    while(cin >> n >> b >> h >> w) {
        int m = 500001;
        for(int i=0, c; i<h; i++) {
            cin >> c;
            for(int j=0, a; j<w; j++) {
                cin >> a;
                if(a >= n && c*n <= b)
                    m = min(m, c * n);
            }
        }
        if(m == 500001)
            cout << "stay home" << endl;
        else
            cout << m << endl;
    }
}
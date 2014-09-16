#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    cout << "Lumberjacks:" << endl;
    while(n-- > 0) {
        int a, b, c = 0;
        cin >> a;
        bool f = true;
        for(int i=0; i<9; i++) {
            cin >> b;
            if(f) {
                if((c > 0 && b-a < 0) || (c < 0 && b-a > 0)) {
                    f = false;
                } else {
                    c = b-a;
                    a = b;
                }
            }

        }
        cout << (f ? "Ordered" : "Unordered") << endl;
    }
}

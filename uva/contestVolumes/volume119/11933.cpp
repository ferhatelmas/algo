#include <bitset>
#include <iostream>

using namespace std;

int main() {
    int n;
    while(cin >> n && n != 0) {
        bitset<32> s(n), a, b;
        bool f = true;
        for(int i=0; i<b.size(); i++) {
            if(s.test(i)) {
                if(f) a.set(i);
                else b.set(i);
                f = !f;
            }
        }
        cout << a.to_ulong() << " " << b.to_ulong() << endl;
    }
}

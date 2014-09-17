#include <iostream>

using namespace std;

int main() {
    int t, n, ns[50];
    cin >> t;
    while(t-- > 0) {
        cin >> n;
        for(int i=0; i<n; i++) cin >> ns[i];
        int c = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n-1; j++) {
                if(ns[j] > ns[j+1]) {
                    ns[j] ^= ns[j+1];
                    ns[j+1] ^= ns[j];
                    ns[j] ^= ns[j+1];
                    c++;
                }
            }
        }
        cout << "Optimal train swapping takes " << c << " swaps." << endl;
    }
}

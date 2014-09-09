#include <iostream>

using namespace std;

int main() {
    int n;
    while(cin >> n && n > 0)
        cout << (n%9 ? n%9 : 9) << endl;
    return 0;
}

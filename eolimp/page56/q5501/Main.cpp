#include <iostream>
#include <sstream>
#include <climits>

using namespace std;

int main() {
    string line;
    int i = 1, m, n = INT_MIN, j;

    while(getline(cin, line)) {
        istringstream is(line);
        while(is >> m) {
            if(m > n) {
                n = m;
                j = i;
            }
        }
        i++;
    }
    if(n != INT_MIN)
        cout << n << " " << j << endl;
}

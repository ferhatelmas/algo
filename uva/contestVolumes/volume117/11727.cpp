#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, a, b, c;
    cin >> n;
    for(int i=1; i<=n; i++) {
        cin >> a >> b >> c;
        vector<int> v {a, b, c};
        sort(v.begin(), v.end());
        cout << "Case " << i << ": " << v[1] << endl;
    }
}
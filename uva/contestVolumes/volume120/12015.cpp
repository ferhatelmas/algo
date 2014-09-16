#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n;
    string s;
    for(int j=1; j<=n; j++) {
        unordered_map<int, vector<string>> h;
        int mm = 0;
        for(int i=0; i<10; i++) {
            cin >> s >> m;
            mm = max(m, mm);
            auto it = h.find(m);
            if(it == h.end()) {
                h[m] = vector<string> {s};
            } else {
                h[m].push_back(s);
            }
        }
        cout << "Case " << "#" << j << ":" << endl;
        for(auto it=h[mm].begin(); it != h[mm].end(); it++)
            cout << (*it) << endl;
    }
}

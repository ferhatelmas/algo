#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int n;
    vector<int> v;
    unordered_map<int, int> m;
    while(cin >> n) {
        if(m.find(n) != m.end())
            m[n]++;
        else {
            m[n] = 1;
            v.push_back(n);
        }
    }

    for(int i=0; i<v.size(); i++)
        cout << v[i] << " " << m[v[i]] << endl;
}

/*
ID: elmas.f2
LANG: C++11
TASK: gift1
*/
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main() {
    ofstream fout ("gift1.out");
    ifstream fin ("gift1.in");
    int n, m;
    string name;
    vector<string> names;
    map<string, int> money;
    fin >> n;
    while(n-- > 0) {
        fin >> name;
        names.push_back(name);
        money[name] = 0;
    }
    int i = names.size();
    while(i-- > 0) {
        fin >> name >> m >> n;
        if(n > 0) {
            money[name] += -m + (m % n);
            m /= n;
            while(n-- > 0) {
                fin >> name;
                money[name] += m;
            }
        }
    }
    for(auto it = names.begin(); it != names.end(); it++) {
        fout << (*it) << " " << money[*it] << endl;
    }
    return 0;
}
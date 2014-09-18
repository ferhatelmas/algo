#include <iostream>
#include <map>
#include <string>

using namespace std;

map<string, int> m;
char buf[6];
int n = 1;

void gen(int curr, int up, int c) {
    if(curr == up) {
        buf[curr] = '\0';
        m[string(buf)] = n++;
        return;
    }
    for(int i=c; i<='z'-up+curr+1; i++) {
        buf[curr] = i;
        gen(curr+1, up, i+1);
    }
}

int main() {
    for(int i=1, j=0; i<6; i++)
        gen(0, i, 'a');

    string s;
    while(cin >> s)
        cout << (m.count(s) == 0 ? 0 : m[s]) << endl;
    return 0;
}

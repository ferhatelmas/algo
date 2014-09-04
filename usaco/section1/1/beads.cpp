/*
ID: elmas.f2
LANG: C++11
TASK: beads
*/
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("beads.out");
    ifstream fin ("beads.in");

    int n, m = 0;
    string s;
    fin >> n >> s;

    for(int i=0, c1, c2; i<n; i++) {
        c1 = c2 = 0;

        for(int j=i, p='w'; j<n+i; j++, c1++)
            if((s[j % n] == 'r' && p == 'b') || (s[j % n] == 'b' && p == 'r'))
                break;
            else if(p == 'w')
                p = s[j % n];

        for(int j=i-1, p='w'; j>i-1-n; j--, c2++)
            if((s[(j + n) % n] == 'r' && p == 'b') || (s[(j + n) % n] == 'b' && p == 'r'))
                break;
            else if(p == 'w')
                p = s[(j + n) % n];

        if(c1 + c2 > n) {
            m = n;
            break;
        }

        m = max(m, c1+c2);
    }
    fout << m << endl;
    return 0;
}

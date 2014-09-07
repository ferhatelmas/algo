#include <iostream>

using namespace std;

char c[100][100];

int main() {
    int n, m, k = 1;
    cin >> n >> m;
    string s;
    while(n != 0 && m != 0) {
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                cin >> c[i][j];

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(c[i][j] == '.') {
                    int cc = 0;
                    if(i > 0 && j > 0) cc += c[i-1][j-1] == '*';
                    if(i > 0) cc += c[i-1][j] == '*';
                    if(i > 0 && j < m-1) cc += c[i-1][j+1] == '*';
                    if(j > 0) cc += c[i][j-1] == '*';
                    if(j < m-1) cc += c[i][j+1] == '*';
                    if(i < n-1 && j > 0) cc += c[i+1][j-1] == '*';
                    if(i < n-1) cc += c[i+1][j] == '*';
                    if(i < n-1 && j < m-1) cc += c[i+1][j+1] == '*';
                    c[i][j] = cc + '0' ;
                }
            }
        }

        if(k > 1) cout << endl;
        cout << "Field #" << (k++) << ":" << endl;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++)
                cout << c[i][j];
            cout << endl;
        }
        cin >> n >> m;
    }
}

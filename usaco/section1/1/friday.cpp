/*
ID: elmas.f2
LANG: C++11
TASK: friday
*/
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main() {
    ofstream fout ("friday.out");
    ifstream fin ("friday.in");
    int n, c[7], d = 0;
    fin >> n;
    memset(c, 0, sizeof(int) * 7);
    for(int i=1900, k=1900+n; i<k; i++) {
      for(int j=0; j<12; j++) {
        c[(d + 5)%7]++;
        if(j == 1) {
          d += i%100 == 0 ? i%400 == 0 : i%4 == 0;
        } else if(j == 3 || j == 5 || j == 8 || j == 10) {
          d += 2;
        } else {
          d += 3;
        }
      }
    }
    fout << c[5] << " " << c[6];
    for(int i=0; i<5; i++)
      fout << " " << c[i];
    fout << endl;
    return 0;
}

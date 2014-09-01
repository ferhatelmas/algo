/*
ID: elmas.f2
LANG: C++11
TASK: ride
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int get_number(string);

int main() {
    ofstream fout ("ride.out");
    ifstream fin ("ride.in");
    string a, b;
    fin >> a >> b;
    int ai = get_number(a), bi = get_number(b);
    fout << (ai%47 == bi%47 ? "GO" : "STAY") << endl;
    return 0;
}

int get_number(string s) {
    int mul = 1;
    for (auto i = s.begin(); i != s.end(); ++i)
        mul *= (*i - 'A' + 1);
    return mul;
}
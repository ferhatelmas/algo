#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>

using namespace std;

string punc(",.:;!?\"()\t\n");

char my_transform(char ch) {
    return punc.find(ch) < punc.size() ? ' ' : ::tolower(ch);
}

int main() {
    int c = 0;
    string s;
    unordered_map<string, int> m;

    while(getline(cin, s)) {
        if(s == "****END_OF_INPUT****") break;
        if(s == "****END_OF_TEXT****") {
            double e_max = log10(c), e_t = 0;
            for(auto it=m.begin(); it!=m.end(); it++)
               e_t += it->second * (e_max - log10(it->second));
            e_t /= c;
            printf("%d %.1lf %.0lf\n", c, e_t, e_t * 100 / e_max);
            m.clear();
            c = 0;
            continue;
        }
        transform(s.begin(), s.end(), s.begin(), my_transform);
        stringstream ss(s);
        while(ss >> s) {
            if(m.find(s) == m.end()) m[s] = 1;
            else m[s]++;
            c++;
        }
    }
    return 0;
}

#include <iostream>
#include <map>

using namespace std;

int main() {
    map<string, string> m = {
        { "HELLO", "ENGLISH" },
        { "HOLA", "SPANISH" },
        { "HALLO", "GERMAN" },
        { "BONJOUR", "FRENCH" },
        { "CIAO", "ITALIAN" },
        { "ZDRAVSTVUJTE", "RUSSIAN" }
    };
    string s;
    int i = 1;
    while(getline(cin, s)) {
        if(s == "#") break;
        else {
            auto it = m.find(s);
            cout << "Case " << (i++) << ": " << (it != m.end() ? it->second : "UNKNOWN") << endl;
        }
    }
}

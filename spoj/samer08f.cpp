#include <iostream>

using namespace std;

int main() {
  long long n;
  while (cin >> n && n != 0) {
    cout << (2 * n + 1) * n * (n + 1) / 6 << endl;
  }
}

#include <cmath>
#include <iostream>

using namespace std;

int main() {
  int a, b;
  while (cin >> a >> b && !(a == 0 && a == 0)) {
    cout << int(floor(sqrt(b)) - ceil(sqrt(a))) + 1 << endl;
  }
}

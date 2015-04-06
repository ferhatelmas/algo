#include <cmath>
#include <iostream>

using namespace std;

int main() {
  int t, a, b;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> a >> b;
    cout << "Case " << i << ": ";
    cout << pow((b + 1) / 2, 2) - pow((a - a % 2) / 2, 2) << endl;
  }
}

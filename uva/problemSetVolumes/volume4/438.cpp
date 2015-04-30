#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

int main() {
  double x1, x2, x3, y1, y2, y3;
  double a1, a2, b1, b2, c1, c2;
  double h, k, r, ans, d;

  while(cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3) {
    a1 = 2 * (x2 - x1);
    a2 = 2 * (x3 - x2);
    b1 = 2 * (y2 - y1);
    b2 = 2 * (y3 - y2);
    c1 = x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2;
    c2 = x2 * x2 + y2 * y2 - x3 * x3 - y3 * y3;

    d = a1 * b2 - a2 * b1;
    h = (b1 * c2 - b2 * c1) / d;
    k = (a2 * c1 - a1 * c2) / d;
    r = sqrt((h - x1) * (h - x1) + (k - y1) * (k - y1));
    ans = 2 * 3.141592653589793 * r;
    cout << fixed << setprecision(2) << ans << endl;
  }
}

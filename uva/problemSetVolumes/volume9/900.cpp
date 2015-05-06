#include <iostream>

using namespace std;

long cache[51] = {0, 1, 2};

int main() {
  for (int i = 3; i < 51; i++) {
    cache[i] = cache[i-1] + cache[i-2];
  }

  int n;
  while (cin >> n && n != 0) {
    cout << cache[n] << endl;
  }
}

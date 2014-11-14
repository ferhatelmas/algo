#include <cstdio>
#include <vector>

using namespace std;

vector<int> primes;

int totient(int n) {
    int r = n;
    for(vector<int>::iterator p=primes.begin(); p!=primes.end(); p++) {
      if(*p > n) break;
      else if(n % *p == 0) r = r * (*p-1) / *p;
    }
    return r;
}

int main() {
    int n, c = 0;
    scanf("%d", &n);
    bool *b = new bool[n+1];
    for(int i=2; i<=n; i++)
        b[i] = true;

    for(int i=2; i<=n; i++)
        if(b[i]) {
            primes.push_back(i);
            for(int j=2*i; j<=n; j+=i)
              b[j] = false;
        }

    for(int i=2; i<=n; i++)
        c += totient(i);

    printf("%d\n", c);
    return 0;
}

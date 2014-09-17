#include <cstdio>

using namespace std;

int main() {
    int n, h, m;
    scanf("%d", &n);
    while(n-- > 0) {
        scanf("%d:%d", &h, &m);
        m = (60 - m) % 60;
        h = 12 - h;
        if(m != 0) h--;
        h = (h+12)%12;
        printf("%02d:%02d\n", (h == 0 ? 12 : h), m);
    }
}

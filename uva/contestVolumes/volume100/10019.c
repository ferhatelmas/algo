#include <stdio.h>

int main() {
    int n, m, b1, b2, i, c;
    scanf("%d\n", &n);
    while(n-- > 0) {
        scanf("%d\n", &m);
        c = m;
        for(i=8192, b1=0; i>0; i/=2) {
            if(c >= i) {
                b1++;
                c -= i;
            }
        }

        for(i=1000, b2=0; i>0; i/=10) {
            switch(m/i) {
                case 0: break;
                case 1:
                case 2:
                case 4:
                case 8: b2++; break;
                case 3:
                case 5:
                case 6:
                case 9: b2 += 2; break;
                case 7: b2 += 3; break;
            }
            m -= (m/i)*i;
        }
        printf("%d %d\n", b1, b2);
    }
    return 0;
}

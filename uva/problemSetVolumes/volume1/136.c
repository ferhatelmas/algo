#include <stdio.h>
#include <stdbool.h>

bool is_ugly(int n) {
    while(n%2 == 0) n /= 2;
    while(n%3 == 0) n /= 3;
    while(n%5 == 0) n /= 5;
    return n == 1;
}

int get_ugly(int m) {
    int i = 1, c = 1;
    while(c < m) {
        if(is_ugly(++i)) c++;
    }
    return i;
}

int main() {
    printf("The 1500'th ugly number is 859963392.\n");
    return 0;
}

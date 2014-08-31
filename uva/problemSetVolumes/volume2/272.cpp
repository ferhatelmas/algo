#include <cstdio>

int main() {
	int c, i = 0, t;
	while((c = getchar()) != EOF) {
		if(c == '"') {
                        t = i++ == 0 ? '`' : '\'';
			putchar(t);
			putchar(t);
			i %= 2;
		} else {
			putchar(c);
		}
	}
	return 0;
}

package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	l, best, p := len(s), 1, 0
	for i := 1; i < l; i++ {
		c := 0
		for j := 1; i-j >= 0 && i+j < l && s[i-j] == s[i+j]; j++ {
			c++
		}
		k := 2*c + 1
		if k > best {
			best, p = k, i-c
		}
	}

	for i := 0; i+1 < l; i++ {
		if s[i] == s[i+1] {
			c := 0
			for j := 1; i-j >= 0 && i+j+1 < l && s[i-j] == s[i+j+1]; j++ {
				c++
			}
			k := 2*c + 2
			if k > best || (k == best && i-c < p) {
				best, p = k, i-c
			}
		}

	}
	fmt.Println(s[p : p+best])
}

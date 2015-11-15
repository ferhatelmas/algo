package main

import "fmt"

func main() {
	var n, s, m, k int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		s += k
		if k > m {
			m = k
		}
	}
	fmt.Println(s + m)
}

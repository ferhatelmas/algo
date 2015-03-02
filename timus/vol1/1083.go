package main

import "fmt"

func main() {
	var n int
	var s string
	fmt.Scan(&n)
	fmt.Scan(&s)
	r, k := 1, len(s)
	for i := n; i > 0; i -= k {
		r *= i
	}
	fmt.Println(r)
}

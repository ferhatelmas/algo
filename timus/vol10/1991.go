package main

import "fmt"

func main() {
	var n, k, e int
	fmt.Scan(&n)
	fmt.Scan(&k)
	a, b := 0, 0
	for i := 0; i < n; i++ {
		fmt.Scan(&e)
		if e > k {
			a += e - k
		} else {
			b += k - e
		}
	}
	fmt.Printf("%d %d\n", a, b)
}

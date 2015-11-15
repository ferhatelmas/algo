package main

import "fmt"

func main() {
	var n, s, t int64
	var k int
	fmt.Scan(&n)
	fmt.Scan(&k)
	for i := 0; i < k; i++ {
		fmt.Scan(&t)
		s += n - t
	}
	n -= s
	if n < 0 {
		n = 0
	}
	fmt.Println(n)
}

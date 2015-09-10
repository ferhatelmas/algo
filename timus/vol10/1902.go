package main

import "fmt"

func main() {
	var t, s, k float64
	var n int
	fmt.Scan(&n)
	fmt.Scan(&t)
	fmt.Scan(&s)
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		fmt.Printf("%.6f\n", (s+t+k)/2)
	}
}

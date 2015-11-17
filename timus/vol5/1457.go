package main

import "fmt"

func main() {
	var n, o int
	var sum float64
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&o)
		if o < 0 {
			o = 0 - o
		}
		sum += float64(o)
	}
	fmt.Printf("%.6f\n", sum/float64(n))
}

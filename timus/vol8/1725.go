package main

import (
	"fmt"
	"math"
)

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)
	if k > n/2 {
		k = n - k + 1
	}
	fmt.Println(math.Max(0, float64(n-k-2)))
}

package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
	}
	sort.Float64s(ns)
	c := ns[n-1]
	for i := n - 2; i > -1; i-- {
		c = 2 * math.Sqrt(c*ns[i])
	}
	fmt.Printf("%.2f", c)
}

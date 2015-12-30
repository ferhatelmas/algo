package main

import (
	"fmt"
	"math"
)

func main() {
	var l, k, h float64
	fmt.Scan(&l)
	fmt.Scan(&k)
	fmt.Scan(&h)
	n := l / k
	fmt.Printf("%.6f %.6f\n", math.Floor(n)*h, math.Ceil(n)*h)
}

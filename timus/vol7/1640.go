package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	var x, y, d float64
	x0, y0 := 0.5, 0.5
	for fmt.Scan(&n); n > 0; n-- {
		fmt.Scan(&x)
		fmt.Scan(&y)
		t := math.Sqrt(math.Pow(x-x0, 2) + math.Pow(y-y0, 2))
		if t > d {
			d = t
		}
	}
	fmt.Printf("%.9f %.9f %.9f\n", x0, y0, d)
}

package main

import (
	"fmt"
	"math"
)

func main() {
	var r float64
	fmt.Scan(&r)
	var x, y, t, r2 float64 = r, 0, 0, r * r
	for x > y {
		y++
		t += 8*(x-y) + 4
		x = math.Ceil(math.Sqrt(r2 - y*y))
	}
	fmt.Printf("%.f\n", t)
}

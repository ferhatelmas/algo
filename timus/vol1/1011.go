package main

import (
	"fmt"
	"math"
)

func main() {
	var p, q, m, pp, qq float64
	fmt.Scan(&q)
	fmt.Scan(&p)
	for p, q, m = 100/p, 100/q, 1; ; m++ {
		pp, qq = math.Floor(m*p), m*q
		if math.Abs(math.Floor(m*q)-qq) > 0.000001 {
			qq = math.Floor(qq) + 1
		}
		if qq-pp >= 2 {
			break
		}
	}
	fmt.Printf("%.0f\n", pp+1)
}

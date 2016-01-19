package main

import (
	"fmt"
	"math"
)

func c(t int, s float64) float64 {
	if t == 1 {
		return 2 * s
	} else if t == 2 {
		return s
	}
	return s * math.Sqrt(3) / 2
}

func main() {
	var n, t, res int
	var s float64

	fmt.Scan(&t)
	fmt.Scan(&s)

	d := c(t, s)
	if t == 2 {
		d = math.Sqrt(2) * s
	}
	if t == 3 {
		d = s
	}

	for fmt.Scan(&n); n > 0; n-- {
		fmt.Scan(&t)
		fmt.Scan(&s)
		if d >= c(t, s) {
			res++
		}
	}
	fmt.Println(res)
}

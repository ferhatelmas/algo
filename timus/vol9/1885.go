package main

import (
	"fmt"
	"math"
)

func main() {
	var h, t, v, x float64
	fmt.Scan(&h)
	fmt.Scan(&t)
	fmt.Scan(&v)
	fmt.Scan(&x)
	fmt.Printf("%.7f %.7f\n", math.Max(0, t-(h-t*v)/(x-v)), math.Min(t, h/x))
}

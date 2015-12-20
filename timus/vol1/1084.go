package main

import (
	"fmt"
	"math"
)

func main() {
	var l, r, res float64
	fmt.Scan(&l)
	fmt.Scan(&r)
	if 2*r*r >= l*l {
		res = l * l
	} else if 2*r <= l {
		res = math.Pi * r * r
	} else {
		res = l*math.Sqrt(4*r*r-l*l) + (math.Pi-4*math.Acos(l/2/r))*r*r
	}
	fmt.Printf("%.3f\n", res)
}

package main

import (
	"fmt"
	"math"
)

func main() {
	var v, a, k float64
	fmt.Scan(&v)
	fmt.Scan(&a)
	fmt.Scan(&k)

	if a == 0 {
		fmt.Println("0.00")
	}
	t := math.Sin(2 * a * math.Pi / 180)
	d := t * v * v / 10
	for v >= 0.001 {
		v /= math.Sqrt(k)
		d += t * v * v / 10
	}
	fmt.Printf("%.2f\n", d)
}

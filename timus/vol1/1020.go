package main

import (
	"fmt"
	"math"
)

var x, y []float64

func border(i, j int) float64 {
	return math.Sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]))
}

func main() {
	var n int
	var r float64
	fmt.Scan(&n)
	fmt.Scan(&r)

	x = make([]float64, n, n)
	y = make([]float64, n, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i])
		fmt.Scan(&y[i])
	}

	res := 2*math.Acos(-1.0)*r + border(n-1, 0)
	for i := 1; i < n; i++ {
		res += border(i-1, i)

	}
	fmt.Printf("%.2f\n", res)
}

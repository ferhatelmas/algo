package main

import "fmt"

func dist(x1, y1, x2, y2 float64) float64 {
	dx, dy := x1-x2, y1-y2
	return dx*dx + dy*dy
}

func main() {
	var n int
	fmt.Scan(&n)
	x, y, r := make([]float64, n), make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i])
		fmt.Scan(&y[i])
		fmt.Scan(&r[i])
		r[i] *= r[i]
	}
	var c int
	for i := 0; i < 1000; i++ {
		for j := 0; j < 1000; j++ {
			x1 := (float64(i) + 0.5) / 1000.0
			y1 := (float64(j) + 0.5) / 1000.0
			var k int
			for ; k < n && dist(x1, y1, x[k], y[k]) > r[k]; k++ {
			}
			if k < n {
				c++
			}
		}
	}
	fmt.Printf("%.6f\n", float64(c)*100.0/1000000)
}

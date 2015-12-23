package main

import (
	"fmt"
	"math"
)

func main() {
	var n float64
	fmt.Scan(&n)
	if n == 1 {
		fmt.Println(1)
	} else {
		fmt.Printf("%.9f\n", 1+1/math.Sin(math.Pi/n))
	}
}

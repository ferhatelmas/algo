package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b float64
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Printf("%.9f\n", ((a+b)*(a+b)+2*(math.Sqrt(2)-1)*a*b)/4)
}

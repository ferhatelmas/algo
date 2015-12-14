package main

import (
	"fmt"
	"math"
)

func main() {
	var k1, k2, k3 float64
	fmt.Scan(&k1)
	fmt.Scan(&k2)
	fmt.Scan(&k3)
	fmt.Println(math.Floor((1000 / (1/k1 + 1/k2 + 1/k3)) + .5))
}

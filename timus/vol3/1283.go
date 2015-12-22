package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y, a float64
	fmt.Scan(&x)
	fmt.Scan(&y)
	fmt.Scan(&a)

	if x == 0 || x <= y {
		fmt.Println(0)
	} else {
		fmt.Println(math.Ceil(math.Log(y/x) / math.Log(1-a/100)))
	}
}

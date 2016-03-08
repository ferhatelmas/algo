package main

import (
	"fmt"
	"math"
)

func main() {
	var l, h, w float64
	fmt.Scan(&l)
	fmt.Scan(&h)
	fmt.Scan(&w)
	if h <= l/2 {
		fmt.Println("butter")
		return
	}
	x := w * math.Sqrt((2*h-l)/981) / 60
	diff := x - float64(int(x))
	if diff > 0.25 && diff < 0.75 {
		fmt.Println("bread")
	} else {
		fmt.Println("butter")
	}
}

package main

import (
	"fmt"
	"math"
)

func main() {
	var n, k float64
	fmt.Scan(&n)
	fmt.Scan(&k)

	p := math.Ceil(math.Log2(math.Min(n/2+1, k)))
	n -= math.Pow(2, p)
	if n > 0 {
		p += n / k
		if int(n)%int(k) > 0 {
			p += 1
		}
	}
	fmt.Println(int(p))
}

package main

import (
	"fmt"
	"math"
)

const l = 10000

func main() {
	var n, m, k int
	fmt.Scan(&n)
	fmt.Scan(&m)
	fmt.Scan(&k)
	a := make([]int, l)
	for i := 0; i < l; i++ {
		c, sqrt := 0, int(math.Sqrt(float64(i)))
		for j := 1; j <= sqrt; j++ {
			if i%j == 0 {
				c++
			}
		}
		a[i] = c
	}
	for i := k; i < l; i++ {
		if a[i] == m && a[i-k] == n {
			fmt.Println(i)
			return
		}
	}
	fmt.Println(0)
}

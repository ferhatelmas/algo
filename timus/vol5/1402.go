package main

import (
	"fmt"
	"math/big"
)

func f(n int) *big.Int {
	r := big.NewInt(1)
	for i := 2; i <= n; i++ {
		r.Mul(r, big.NewInt(int64(i)))
	}
	return r
}

func main() {
	var n int
	fmt.Scan(&n)
	if n == 1 {
		fmt.Println(0)
	} else if n == 2 {
		fmt.Println(2)
	} else {
		r, t := big.NewInt(0), f(n)
		for i := 2; i <= n; i++ {
			r.Add(r, new(big.Int).Div(t, f(n-i)))
		}
		fmt.Println(r)
	}
}

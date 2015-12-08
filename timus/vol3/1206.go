package main

import (
	"fmt"
	"math/big"
)

func main() {
	var k int64
	fmt.Scan(&k)
	r := big.NewInt(k - 1)
	r.Exp(big.NewInt(55), r, nil)
	r.Mul(r, big.NewInt(36))
	fmt.Println(r)
}

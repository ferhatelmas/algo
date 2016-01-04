package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int
	fmt.Scan(&n)

	ans, three := big.NewInt(1), big.NewInt(3)
	if n%3 == 1 && n > 1 {
		ans = big.NewInt(4)
		n -= 4
	} else if n%3 == 2 {
		ans = big.NewInt(2)
		n -= 2
	}

	for i := n/3 - 1; i >= 0; i-- {
		ans.Mul(ans, three)
	}
	fmt.Println(ans)
}

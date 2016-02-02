package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)

	x := big.NewInt(int64(k) - 1)
	dp := make([][]*big.Int, n)

	dp[1] = []*big.Int{new(big.Int).Add(x, big.NewInt(1)), x}
	for i := 2; i < n; i++ {
		dp[i] = []*big.Int{
			new(big.Int).Add(new(big.Int).Mul(dp[i-1][0], x), dp[i-1][1]),
			new(big.Int).Mul(dp[i-1][0], x),
		}
	}
	fmt.Println(new(big.Int).Mul(dp[n-1][0], x))
}

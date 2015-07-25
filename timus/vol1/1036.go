package main

import (
	"fmt"
	"math/big"
)

func up(j int) int {
	if j < 9 {
		return j
	}
	return 9
}

func main() {
	var n, s int
	fmt.Scan(&n)
	fmt.Scan(&s)
	if s%2 == 1 {
		fmt.Println(0)
	} else {
		s /= 2
		dp := make([][]*big.Int, n+1, n+1)
		for i := 0; i <= n; i++ {
			dp[i] = make([]*big.Int, s+1, s+1)
			for j := 0; j <= s; j++ {
				dp[i][j] = &big.Int{}
			}
		}
		dp[0][0] = big.NewInt(1)
		for i := 1; i <= n; i++ {
			for j := 0; j <= s; j++ {
				for k := 0; k <= up(j); k++ {
					dp[i][j].Add(dp[i][j], dp[i-1][j-k])
				}
			}
		}
		fmt.Println(dp[n][s].Mul(dp[n][s], dp[n][s]))
	}
}

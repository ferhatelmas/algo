package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	dp := make([]int, 56)
	dp[1] = 1
	dp[2] = 1
	dp[3] = 2

	for i := 4; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-3] + 1
	}
	fmt.Println(dp[n])
}

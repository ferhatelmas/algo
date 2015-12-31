package main

import "fmt"

func main() {
	dp := make([][]int, 11)
	for i := 0; i < 11; i++ {
		dp[i] = make([]int, 11)
		dp[i][0], dp[i][i] = 1, 1
		for j := 1; j < i; j++ {
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
		}
	}
	counts := make([]int, 11)
	counts[0] = 1
	for i := 1; i < 11; i++ {
		for j := 1; j <= i; j++ {
			counts[i] += dp[i][j] * counts[i-j]
		}
	}
	var n int
	for {
		fmt.Scan(&n)
		if n == -1 {
			break
		}
		fmt.Println(counts[n])
	}
}

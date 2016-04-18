package main

import "fmt"

var dp [44][2]int

func print(k, n int) {
	if n == 0 {
		return
	}
	if k < dp[n][0] {
		fmt.Print(0)
		print(k, n-1)
	} else {
		fmt.Print(1)
		print(k-dp[n][0], n-1)
	}
}

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)

	dp[1][0], dp[1][1] = 1, 1
	for i := 2; i <= n; i++ {
		dp[i][0], dp[i][1] = dp[i-1][0]+dp[i-1][1], dp[i-1][0]
	}
	if dp[n][0]+dp[n][1] < k {
		fmt.Println(-1)
	} else {
		print(k-1, n)
	}
}

package main

import "fmt"

func max(ns []int) int {
	n := ns[0]
	for _, k := range ns[1:] {
		if k > n {
			n = k
		}
	}
	return n
}

func mod(a int) int {
	return a % 1000000007
}

func main() {
	var n, a, b int
	fmt.Scan(&n)
	fmt.Scan(&a)
	fmt.Scan(&b)

	m := []int{a, b}
	dp := make([][][]int, 2)
	for i := 0; i < 2; i++ {
		dp[i] = make([][]int, 2)
		for j := 0; j < 2; j++ {
			dp[i][j] = make([]int, max(m)+1)
			if i == 0 {
				dp[i][j][0], dp[i][j][1] = 1, 1
			}
		}
	}

	for i := 1; i < n; i++ {
		for j := 0; j < 2; j++ {
			dp[i%2][j][0] = 0
		}
		for j := 0; j < 2; j++ {
			for k := 1; k <= m[j]; k++ {
				t := dp[(i-1)%2][j][k-1]
				dp[i%2][j][k] = t
				dp[i%2][1-j][0] = mod(dp[i%2][1-j][0] + t)
			}
		}
	}
	fmt.Println(mod(dp[(n-1)%2][0][0] + dp[(n-1)%2][1][0]))
}

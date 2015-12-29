package main

import "fmt"

var dp [901][8101]int

func main() {
	for i := 0; i < 901; i++ {
		for j := 0; j < 8101; j++ {
			dp[i][j] = -1
		}
	}
	dp[0][0] = 0
	for i := 1; i < 901; i++ {
		for j := 0; j < 8101; j++ {
			for k := 1; k < 10; k++ {
				if i >= k && j >= k*k && dp[i-k][j-k*k] != -1 {
					t := 1 + dp[i-k][j-k*k]
					if t <= 100 && (dp[i][j] == -1 || t < dp[i][j]) {
						dp[i][j] = t
					}
				}
			}
		}
	}

	var n, s, q int
	for fmt.Scan(&n); n > 0; n-- {
		fmt.Scan(&s)
		fmt.Scan(&q)
		if s > 900 || q > 8100 || dp[s][q] == -1 {
			fmt.Println("No solution")
			continue
		}
		for s > 0 || q > 0 {
			for i := 1; i < 10; i++ {
				if s >= i && q >= i*i && 1+dp[s-i][q-i*i] == dp[s][q] {
					fmt.Print(i)
					s, q = s-i, q-i*i
					break
				}
			}
		}
		fmt.Println()
	}
}

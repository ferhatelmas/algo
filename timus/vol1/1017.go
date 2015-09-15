package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([][]int64, n+1, n+1)
	for i := 0; i <= n; i++ {
		ns[i] = make([]int64, n+1, n+1)
	}
	for i := 0; i <= n; i++ {
		ns[0][i] = 1
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			ns[i][j] = ns[i][j-1]
			if j <= i {
				ns[i][j] += ns[i-j][j-1]
			}
		}
	}
	fmt.Println(ns[n][n-1])
}

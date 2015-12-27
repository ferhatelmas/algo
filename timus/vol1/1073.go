package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n int
	fmt.Scan(&n)

	ns := make([]int, n+1)

	for i := 1; i <= n; i++ {
		ns[i] = i + 1
		for j := 1; j*j <= i; j++ {
			ns[i] = min(ns[i], ns[i-j*j]+1)
		}
	}
	fmt.Println(ns[n])
}

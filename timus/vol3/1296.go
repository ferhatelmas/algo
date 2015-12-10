package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n, k int
	fmt.Scan(&n)
	var s, m int
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		s = max(0, s+k)
		m = max(m, s)
	}
	fmt.Println(m)
}

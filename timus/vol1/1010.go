package main

import "fmt"

func abs(a int64) int64 {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		fmt.Scan(&ns[i])
	}

	r := 1
	for i := 2; i+1 <= n; i++ {
		if abs(ns[i+1]-ns[i]) > abs(ns[r+1]-ns[r]) {
			r = i
		}
	}
	fmt.Printf("%d %d\n", r, r+1)
}

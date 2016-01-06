package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)
	ns := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
	}

	for i, j := 0, (n+k-1)/k; i < j; i++ {
		for l := i; l < n; l += j {
			fmt.Printf("%4d", ns[l])
		}
		fmt.Println()
	}
}

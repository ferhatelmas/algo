package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n)
	fmt.Scan(&m)
	for i := 1; i <= n; i++ {
		fmt.Printf("%d ", i)
	}
	fmt.Println()
	for i := 1; i <= m; i++ {
		fmt.Printf("%d ", 1+i*n)
	}
}

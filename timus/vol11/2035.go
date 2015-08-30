package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var x, y, c int
	fmt.Scan(&x)
	fmt.Scan(&y)
	fmt.Scan(&c)
	if x+y < c {
		fmt.Println("Impossible")
	} else {
		fmt.Printf("%d %d\n", min(x, c), max(c-x, 0))
	}
}

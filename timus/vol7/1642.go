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
	var n, x, k int
	fmt.Scan(&n)
	fmt.Scan(&x)
	x1, x2 := -1000, 1000
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		if k < 0 {
			x1 = max(x1, k)
		}
		if k > 0 {
			x2 = min(x2, k)
		}
	}

	if x1 < x && x < x2 {
		if x > 0 {
			fmt.Printf("%d %d\n", x, x-2*x1)
		} else {
			fmt.Printf("%d %d\n", 2*x2-x, -x)
		}
	} else {
		fmt.Println("Impossible")
	}
}

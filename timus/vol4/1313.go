package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([][]int, n)
	for i := range ns {
		ns[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Scan(&ns[i][j])
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			fmt.Print(ns[i-j][j], " ")
		}
	}
	for i := 1; i < n; i++ {
		for j := i; j <= n-1; j++ {
			fmt.Print(ns[n-1+i-j][j])
			if i != n-1 || j != n-1 {
				fmt.Print(" ")
			}
		}
	}
	fmt.Println()
}


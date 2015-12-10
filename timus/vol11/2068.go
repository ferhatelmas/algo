package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)
	var wins = true
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		if k/2%2 == 0 {
			wins = !wins
		}
	}
	if wins {
		fmt.Println("Daenerys")
	} else {
		fmt.Println("Stannis")
	}
}

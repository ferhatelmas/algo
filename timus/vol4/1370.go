package main

import "fmt"

func main() {
	var n, m int
	d := make([]int, 1000, 1000)
	fmt.Scan(&n)
	fmt.Scan(&m)
	for i := 0; i < n; i++ {
		fmt.Scan(&d[i])
	}
	for i := 0; i < 10; i++ {
		fmt.Print(d[(m+i)%n])
	}
}

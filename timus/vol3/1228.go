package main

import "fmt"

func main() {
	var n, k, m int
	fmt.Scan(&n)
	fmt.Scan(&k)
	for i := 0; i < n; i++ {
		fmt.Scan(&m)
		fmt.Println(k/m - 1)
		k = m
	}
}

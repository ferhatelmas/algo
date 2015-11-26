package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)
	fmt.Println(n*(n-1)/2 - k)
}

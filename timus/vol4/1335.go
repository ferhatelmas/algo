package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	n2 := n * n
	fmt.Printf("%d %d %d", n2+2*n, n2+n, n2)
}

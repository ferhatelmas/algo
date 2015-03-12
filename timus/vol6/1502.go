package main

import "fmt"

func main() {
	var n int64
	fmt.Scan(&n)
	fmt.Println((n * (n + 1) / 2) * (n + 2))
}

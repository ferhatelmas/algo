package main

import "fmt"

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func main() {
	var n, m int
	fmt.Scan(&n)
	fmt.Scan(&m)
	fmt.Println(n + m - 2 - gcd(n-1, m-1))
}

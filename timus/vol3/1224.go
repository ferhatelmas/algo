package main

import "fmt"

func main() {
	var n, m int64
	fmt.Scan(&n)
	fmt.Scan(&m)
	if n > m {
		fmt.Println(2*(m-1) + 1)
	} else {
		fmt.Println(2 * (n - 1))
	}
}

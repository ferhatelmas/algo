package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)

	m := make(map[int]int, n)
	for i := n; i > 0; i-- {
		fmt.Scan(&k)
		m[k]++
	}

	k = 0
	for _, i := range m {
		k += i / 4
	}
	fmt.Println(k)
}

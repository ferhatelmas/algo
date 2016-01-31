package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)

	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		a[((i-k+1)%n+n)%n]++
	}

	var best, pos int
	for i, v := range a {
		if v > best {
			best, pos = v, i
		}
	}
	fmt.Println(pos + 1)
}

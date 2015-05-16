package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, k int
	fmt.Scan(&n)
	ns := make([]int, n, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
	}
	sort.Ints(ns)
	var s string
	fmt.Scan(&s)
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&k)
		fmt.Println(ns[k-1])
	}
}

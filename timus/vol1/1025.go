package main

import (
	"fmt"
	"sort"
)

func main() {
	var k int
	fmt.Scan(&k)
	ns := make([]int, k)
	for i := 0; i < k; i++ {
		fmt.Scan(&ns[i])
	}
	sort.Ints(ns)
	r := 0
	for i := k / 2; i > -1; i-- {
		r += ns[i]/2 + 1
	}
	fmt.Println(r)
}

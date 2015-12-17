package main

import (
	"fmt"
	"math"
	"sort"
)

func read(n int) []int {
	ls := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ls[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(ls)))
	return ls
}

func sum(ls []int) int {
	var s int
	for _, i := range ls {
		s += i
	}
	return s
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n, m int
	fmt.Scan(&n)
	fmt.Scan(&m)
	girls, boys := read(n), read(m)
	t := math.MaxInt32
	for i, k := 0, min(n, m); i <= k; i++ {
		t = min(sum(girls[i:])+i*sum(boys[i:]), t)
	}
	fmt.Println(t)
}

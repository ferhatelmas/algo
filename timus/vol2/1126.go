package main

import (
	"fmt"
)

func max(ints []int) int {
	m := 0
	for _, i := range ints {
		if i > m {
			m = i
		}
	}
	return m
}

func main() {
	var n, k int
	fmt.Scan(&n)
	data := make([]int, n)
	i := 0
	for {
		fmt.Scan(&k)
		if k == -1 {
			break
		}
		data[i%n] = k
		if i >= n-1 {
			fmt.Println(max(data))
		}
		i++
	}
}

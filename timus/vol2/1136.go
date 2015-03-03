package main

import "fmt"

func reverse(ns []int) []int {
	l := len(ns)
	if l < 2 {
		return ns
	}
	c, d := make([]int, l), 0
	for i, v := range ns {
		if v > ns[l-1] {
			d = i
			break
		}
	}

	copy(c[:l-1-d], reverse(ns[d:l-1]))
	copy(c[l-1-d:], reverse(ns[:d]))
	c[l-1] = ns[l-1]
	return c
}

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
	}

	for _, v := range reverse(ns) {
		fmt.Println(v)
	}
}

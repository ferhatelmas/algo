package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)
	ns := make([]int, 17, 17)
	ns[0] = 1
	ns[1] = k - 1
	for i := 2; i <= n; i++ {
		ns[i] = (k - 1) * (ns[i-1] + ns[i-2])
	}
	fmt.Println(ns[n])
}

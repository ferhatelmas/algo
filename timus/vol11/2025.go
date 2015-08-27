package main

import "fmt"

func s(n, k int) int {
	d := n / k
	c := n % k
	ns := make([]int, k, k)
	for i := 0; i < k; i++ {
		ns[i] = d
		if i < c {
			ns[i]++
		}
	}
	res := 0
	for i := 0; i < k-1; i++ {
		for j := i + 1; j < k; j++ {
			res += ns[i] * ns[j]
		}
	}
	return res
}

func main() {
	var t, n, k int
	fmt.Scan(&t)
	for ; t > 0; t-- {
		fmt.Scan(&n)
		fmt.Scan(&k)
		fmt.Println(s(n, k))
	}
}

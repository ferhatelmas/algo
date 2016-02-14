package main

import "fmt"

func nw(n int) []int {
	return make([]int, n+1)
}

func main() {
	var n int
	fmt.Scan(&n)
	ns, a, b := nw(n), nw(n), nw(n)
	for i := 1; i <= n; i++ {
		fmt.Scan(&ns[i])
	}
	for i := 1; i < n; i++ {
		for j := i + 1; j <= n; j++ {
			if ns[i] > ns[j] {
				a[ns[i]]++
				b[ns[j]]++
			}
		}
	}
	for i := 1; i <= n; i++ {
		fmt.Printf("%d %d\n", b[i]+1, n-a[i])
	}
}

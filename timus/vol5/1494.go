package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	ns, ms := make([]int, n), make([]int, n)
	for i := n - 1; i > -1; i-- {
		fmt.Scan(&ns[i])
	}
	p, m := n, 0
	for i := 1; i <= n; i++ {
		ms[m] = i
		m++
		for ; m > 0 && p > 0 && ns[p-1] == ms[m-1]; p, m = p-1, m-1 {
		}
	}
	if p > 0 || m > 0 {
		fmt.Println("Cheater")
	} else {
		fmt.Println("Not a proof")
	}
}

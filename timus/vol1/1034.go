package main

import "fmt"

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func ch(ns []int, ind ...int) int {
	for a := 1; a < len(ns); a++ {
		for _, b := range ind {
			if a != b && abs(ns[a]-ns[b]) == abs(a-b) {
				return 0
			}
		}
	}
	return 1
}

func main() {
	var n, t int
	fmt.Scan(&n)
	ns := make([]int, n+1)
	for i := 0; i < n; i++ {
		fmt.Scan(&t)
		fmt.Scan(&ns[t])
	}

	var ans int
	for i := 1; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k <= n; k++ {
				ns[i], ns[j], ns[k] = ns[j], ns[k], ns[i]
				ans += ch(ns, i, j, k)
				ns[i], ns[j], ns[k] = ns[j], ns[k], ns[i]
				ans += ch(ns, i, j, k)
				ns[i], ns[j], ns[k] = ns[j], ns[k], ns[i]
			}
		}
	}
	fmt.Println(ans)
}

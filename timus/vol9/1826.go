package main

import (
	"fmt"
	"sort"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n, ans int
	fmt.Scan(&n)
	ns := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
	}
	sort.Ints(ns)
	for s, t := 0, n-1; s < t; {
		if t-s == 1 {
			ans, s, t = ans+ns[t], s+1, t-1
		} else if t-s == 2 {
			ans, s, t = ans+ns[t]+ns[t-1]+ns[s], s+1, t-2
		} else {
			ans += min(ns[s+1]+ns[s]+ns[t]+ns[s+1], ns[t]+ns[s]+ns[t-1]+ns[s])
			t -= 2
		}
	}
	fmt.Println(ans)
}

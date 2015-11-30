package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)

	ps := make([][]string, n, n)
	for i := 0; i < n; i++ {
		ln := make([]string, 3, 3)
		for j := 0; j < 3; j++ {
			fmt.Scan(&ln[j])
		}
		sort.Strings(ln)
		ps[i] = ln
	}

	ids := make([]int, n, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ids[i])
		ids[i]--
	}

	chosen := make([]int, n, n)
	for i := 1; i < n; i++ {
		found := false
		for j := 0; j < 3; j++ {
			if ps[ids[i]][j] > ps[ids[i-1]][chosen[i-1]] {
				chosen[i], found = j, true
				break
			}
		}
		if !found {
			fmt.Println("IMPOSSIBLE")
			return
		}
	}
	for i := 0; i < n; i++ {
		fmt.Println(ps[ids[i]][chosen[i]])
	}
}

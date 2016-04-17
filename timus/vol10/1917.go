package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, p int
	fmt.Scan(&n)
	fmt.Scan(&p)
	ns := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ns[i])
	}
	sort.Ints(ns)
	var i, a1, a2, cnt int
	for i < n {
		j := i
		for ; j < n && ns[j] == ns[i]; j++ {
		}
		s := j - i
		if (cnt+s)*ns[i] <= p {
			cnt += s
		} else {
			if cnt == 0 || cnt*ns[i-1] > p {
				break
			}
			a1, a2, cnt = a1+cnt, a2+1, s
		}
		i = j
	}
	if cnt > 0 && cnt*ns[i-1] <= p {
		a1, a2 = a1+cnt, a2+1
	}
	fmt.Printf("%d %d\n", a1, a2)
}

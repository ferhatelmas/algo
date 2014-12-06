package main

import "fmt"

func main() {
	var n, i, j uint
	fmt.Scan(&n)
	ls, m := make([]int, n), 20000000

	for i = 0; i < n; i++ {
		fmt.Scan(&ls[i])
	}
	for i = 1 << n; i > 0; i-- {
		s := 0
		for j = 0; j < n; j++ {
			if i&(1<<j) == 0 {
				s += ls[j]
			} else {
				s -= ls[j]
			}
		}
		if s >= 0 && s < m {
			m = s
		}
	}
	fmt.Println(m)
}

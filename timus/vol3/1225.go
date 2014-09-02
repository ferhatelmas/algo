package main

import "fmt"

var m [][]uint64

func main() {
	var n int
	fmt.Scan(&n)
	m = make([][]uint64, 2)
	for i, _ := range m {
		m[i] = make([]uint64, n)
		for j, _ := range m[i] {
			m[i][j] = 0
		}
	}
	fmt.Println(perm(0, n-1) + perm(1, n-1))
}

func perm(color, j int) uint64 {
	if j == 0 {
		return 1
	} else if m[color][j-1] > 0 {
		return m[color][j-1]
	} else {
		res := perm(1-color, j-1)
		if j >= 2 {
			res += perm(1-color, j-2)
		}
		m[color][j-1] = res
		return res
	}
}

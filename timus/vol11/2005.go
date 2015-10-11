package main

import "fmt"

var p = [][]int{
	[]int{1, 2, 3, 4, 5},
	[]int{1, 3, 2, 4, 5},
	[]int{1, 3, 4, 2, 5},
	[]int{1, 4, 3, 2, 5},
}

func cost(d [5][5]int, v []int) int {
	res := 0
	for i := 0; i < 4; i++ {
		res += d[v[i]-1][v[i+1]-1]
	}
	return res
}

func main() {
	var ns [5][5]int
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			fmt.Scan(&ns[i][j])
		}
	}
	m, idx := 100000, -1
	for i, v := range p {
		if c := cost(ns, v); c < m {
			m, idx = c, i
		}
	}
	fmt.Println(m)
	for _, e := range p[idx] {
		fmt.Printf("%d ", e)
	}
}

package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n int
	fmt.Scan(&n)
	ns := make([][]int, n)
	for i := 0; i < n; i++ {
		ns[i] = make([]int, 3)
		for j := 0; j < 3; j++ {
			fmt.Scan(&ns[i][j])
		}
	}
	for i := 1; i < n; i++ {
		k, j := ns[i], i-1
		for ; j >= 0 && ns[j][0] > k[0]; j-- {
			ns[j+1] = ns[j]
		}
		ns[j+1] = k
	}
	var m, t int
	for i := 0; i < n; i++ {
		t = max(t, ns[i][0]) + ns[i][1]
		m = max(m, t-ns[i][2])
	}
	fmt.Println(m)
}

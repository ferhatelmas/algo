package main

import "fmt"

var n = []int{10, 50, 100, 500, 1000, 5000}

func main() {
	var p, total, min int
	m := make([]int, 6, 6)
	for i := 0; i < 6; i++ {
		fmt.Scan(&m[i])
		total += m[i] * n[i]
		if min == 0 && m[i] > 0 {
			min = n[i]
		}
	}
	fmt.Scan(&p)

	maxCount := total / p
	minCount := 1 + (total-min)/p
	count := maxCount - minCount + 1
	fmt.Println(count)
	for i := 0; i < count; i++ {
		fmt.Printf("%d ", minCount+i)
	}
}

package main

import "fmt"

func main() {
	ls := make([]int, 100000)
	ls[0] = 0
	ls[1] = 1
	for i := 2; i < 100000; i++ {
		if i%2 == 0 {
			ls[i] = ls[i/2]
		} else {
			ls[i] = ls[i/2] + ls[i/2 + 1]
		}
	}

	var k int
	for {
		fmt.Scan(&k)
		if k == 0 {
			break
		}
		fmt.Println(findMax(ls, k))
	}
}

func findMax(ls []int, k int) (m int) {
	m = 0
	for i := 0; i <= k; i++ {
		if ls[i] > m {
			m = ls[i]
		}
	}
	return
}


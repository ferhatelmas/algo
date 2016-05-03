package main

import "fmt"

var dp [10][82]int

func mem(d, s int) int {
	if s < 0 {
		return 0
	} else if d == 0 {
		if s == 0 {
			return 1
		}
		return 0
	}

	r := &dp[d][s]
	if *r == -1 {
		*r = 0
		for i := 0; i < 10; i++ {
			*r += mem(d-1, s-i)
		}
	}
	return *r
}

func main() {
	for i := 0; i < 10; i++ {
		for j := 0; j < 82; j++ {
			dp[i][j] = -1
		}
	}

	var s int
	fmt.Scan(&s)
	r := mem(9, s)
	if s == 1 {
		r++
	}
	fmt.Println(r)
}

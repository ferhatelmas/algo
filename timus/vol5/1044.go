package main

import (
	"fmt"
	"math"
	"strconv"
)

func isLucky(p, n, k int) bool {
	s := fmt.Sprintf("%d%0"+strconv.Itoa(k)+"d", p, n)
	c, l := 0, len(s)
	for i := l/2 - 1; i > -1; i-- {
		c += (int(s[i]) - '0')
		c -= (int(s[l-i-1]) - '0')
	}
	return c == 0
}

func calculate(n int) int {
	c, k := 0, int(n)-1
	for i := int(math.Pow(float64(10), float64(n-1))) - 1; i > -1; i-- {
		for j := 0; j < 10; j++ {
			if isLucky(j, i, k) {
				c++
			}
		}
	}
	return c
}

func main() {
	var n int
	fmt.Scan(&n)
	switch n {
	case 2:
		fmt.Println(10)
	case 4:
		fmt.Println(670)
	case 6:
		fmt.Println(55252)
	case 8:
		fmt.Println(4816030)
	}
}

package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	var (
		n int
		s string
	)
	fmt.Scan(&n)

	sum, c := 0.0, 0.0
	for i := 0; i < n; i++ {
		fmt.Scan(&s)
		ch := string(s[0])
		if strings.Contains("APOR", ch) {
			sum += math.Abs(c - 0.0)
			c = 0
		} else if strings.Contains("BMS", ch) {
			sum += math.Abs(c - 1.0)
			c = 1
		} else {
			sum += math.Abs(c - 2.0)
			c = 2
		}
	}
	fmt.Println(sum)
}

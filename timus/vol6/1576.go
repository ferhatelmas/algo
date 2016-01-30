package main

import (
	"fmt"
	"math"
)

func main() {
	var n1, c1, n2, t, c2, n3, k, m, s, total int
	fmt.Scan(&n1)
	fmt.Scan(&c1)
	fmt.Scan(&n2)
	fmt.Scan(&t)
	fmt.Scan(&c2)
	fmt.Scan(&n3)

	for fmt.Scan(&k); k > 0; k-- {
		fmt.Scanf("%d:%d", &m, &s)
		if m == 0 && s < 7 {
			continue
		}
		total += m
		if s > 0 {
			total++
		}
	}
	fmt.Printf("Basic:     %d\n", n1+c1*total)
	fmt.Printf("Combined:  %d\n", n2+c2*int(math.Max(0, float64(total-t))))
	fmt.Printf("Unlimited: %d\n", n3)
}

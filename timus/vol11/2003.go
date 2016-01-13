package main

import (
	"fmt"
	"math"
	"os"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func update(m map[int]int, t, i int) int {
	m[i]++
	t = max(t, m[i])
	if t > 2 {
		fmt.Println("infinity")
		os.Exit(0)
	}
	return t
}

func main() {
	var n, k, t int
	m := map[int]int{}
	for fmt.Scan(&n); n > 0; n-- {
		fmt.Scan(&k)
		for i, sq := 2, int(math.Sqrt(float64(k))); i <= sq; i++ {
			if k%i == 0 {
				for k%i == 0 {
					k /= i
				}
				t = update(m, t, i)
			}
		}
		if k > 1 {
			t = update(m, t, k)
		}
	}
	fmt.Println(t)
}

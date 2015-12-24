package main

import "fmt"

func main() {
	var n, z int
	fmt.Scan(&n)

	for i := 10; ; i *= 10 {
		r1, r2, r3, r4 := 1, 1, 1, 1
		for j := n; j > 0; j-- {
			r2 = (r2 * 2) % i
			r3 = (r3 * 3) % i
			r4 = (r4 * 4) % i
		}

		if (r1+r2+r3+r4)%i == 0 {
			z++
		} else {
			break
		}
	}
	fmt.Println(z)
}

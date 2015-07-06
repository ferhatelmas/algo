package main

import "fmt"

func main() {
	var n, k int
	var s string
	down, up := 2, 10
	fmt.Scan(&n)
	for ; n > 0; n-- {
		fmt.Scan(&k)
		fmt.Scan(&s)
		if s == "hungry" && down < k {
			down = k
		} else if s == "satisfied" && k < up {
			up = k
		}
	}
	if down < up {
		fmt.Println(up)
	} else {
		fmt.Println("Inconsistent")
	}
}

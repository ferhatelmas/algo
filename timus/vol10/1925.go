package main

import "fmt"

func main() {
	var n, k, t int
	fmt.Scan(&n)
	fmt.Scan(&k)
	k -= 2

	for ; n > 0; n-- {
		fmt.Scan(&t)
		k += t
		fmt.Scan(&t)
		k -= t
		k -= 2
	}

	if k >= 0 {
		fmt.Println(k)
	} else {
		fmt.Println("Big Bang!")
	}
}

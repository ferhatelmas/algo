package main

import "fmt"

func main() {
	var n, x int64
	var m int
	fmt.Scan(&n)
	fmt.Scan(&m)

	n *= 3
	for i := 0; i < m; i++ {
		fmt.Scan(&x)
		n -= x
		if n < 0 {
			fmt.Printf("Free after %d times.\n", i+1)
			return
		}
	}
	fmt.Println("Team.GOV!")
}

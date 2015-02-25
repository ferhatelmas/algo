package main

import "fmt"

func main() {
	var a, b, t int
	fmt.Scan(&a)
	fmt.Scan(&b)
	s := 0
	for i := 0; i < 10; i++ {
		fmt.Scan(&t)
		s += 20 * t
	}
	if b-a >= s {
		fmt.Println("No chance.")
	} else {
		fmt.Println("Dirty debug :(")
	}
}

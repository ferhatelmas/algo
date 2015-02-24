package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a)
	fmt.Scan(&b)
	c := 0
	for ; a <= b; a++ {
		if a%2 == 1 {
			c++
		}
	}
	fmt.Println(c)
}

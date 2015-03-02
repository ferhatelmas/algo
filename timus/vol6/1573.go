package main

import "fmt"

func main() {
	var b, r, y, t int
	fmt.Scan(&b)
	fmt.Scan(&r)
	fmt.Scan(&y)
	fmt.Scan(&t)
	c := 1
	var s string
	for ; t > 0; t-- {
		fmt.Scan(&s)
		if s == "Red" {
			c *= r
		} else if s == "Blue" {
			c *= b
		} else if s == "Yellow" {
			c *= y
		}
	}
	fmt.Println(c)
}

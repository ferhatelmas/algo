package main

import "fmt"

func main() {
	var a, ap, b, bp int
	fmt.Scan(&a)
	fmt.Scan(&ap)
	fmt.Scan(&b)
	fmt.Scan(&bp)
	for a <= b {
		a += ap
		if a > b {
			a = b
		}
		b -= bp
	}
	fmt.Println(a)
}

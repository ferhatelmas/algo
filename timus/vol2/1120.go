package main

import "fmt"

func main() {
	var n, t int
	fmt.Scan(&n)
	for i := 33000; i > 0; i-- {
		t = 2*n - (i-1)*i
		if t > 0 && t%(2*i) == 0 {
			fmt.Println(t/(2*i), i)
			break
		}
	}
}

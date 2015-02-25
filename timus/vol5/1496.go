package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	m := make(map[string]int)
	var s string
	for ; n > 0; n-- {
		fmt.Scan(&s)
		m[s] += 1
	}

	for k, v := range m {
		if v > 1 {
			fmt.Println(k)
		}
	}
}

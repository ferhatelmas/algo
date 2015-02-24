package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)

	m := 0
	for _, e := range s {
		m *= 10
		m += int(e - '0')
		m %= 7
	}
	fmt.Println(m)
}

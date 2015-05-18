package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	n := 0
	for _, c := range s {
		n += int(c - '0')
	}
	n %= 3
	if n == 0 {
		fmt.Println(2)
	} else {
		fmt.Println(1)
		fmt.Println(n)
	}
}

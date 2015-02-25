package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	m := make([]string, n)
	var t string
	for ; n > 0; n-- {
		fmt.Scan(&t)
		m = append(m, t)
	}
	fmt.Scan(&t)
	for _, v := range m {
		if strings.HasPrefix(v, t) {
			fmt.Println(v)
		}
	}
}

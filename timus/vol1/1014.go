package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	if n == 0 {
		fmt.Println(10)
	} else if n == 1 {
		fmt.Println(1)
	} else {
		var r []string
		for i := 9; i > 1; i-- {
			for n%i == 0 {
				r = append(r, fmt.Sprintf("%d", i))
				n /= i
			}
		}
		if n == 1 {
			sort.Strings(r)
			fmt.Println(strings.Join(r, ""))
		} else {
			fmt.Println(-1)
		}
	}
}

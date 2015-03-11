package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, c int
	cs := make([]int, 3)
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&c)
		cs[c-1]++
	}
	sort.Ints(cs)
	if n > 5 {
		if cs[1] > 0 {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	} else {
		switch n {
		case 1, 2:
			fmt.Println("No")
		case 3:
			if cs[0] > 0 {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		case 4:
			if (cs[0] > 0) || cs[1] > 1 {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		case 5:
			if (cs[1] > 1) || ((cs[1] > 0) && (cs[0] > 0)) {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		}
	}
}

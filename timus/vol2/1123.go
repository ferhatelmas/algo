package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	ln := len(s)
	mid, odd := ln/2, ln%2
	ls := []rune(s)
	for i := 0; i < mid; i++ {
		l, r := ls[mid-i-1], ls[mid+i+odd]
		if r < l {
			break
		} else if l < r {
			j := mid + odd - 1
			for ; j > -1; j-- {
				if s[j] < '9' {
					ls[j] += 1
					break
				}
			}
			for j = j + 1; j < mid+odd; j++ {
				ls[j] = '0'
			}
			break
		}
	}
	for i := 0; i < mid; i++ {
		ls[ln-i-1] = ls[i]
	}
	fmt.Println(string(ls))
}

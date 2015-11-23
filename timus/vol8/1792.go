package main

import "fmt"

func t(ns []int) bool {
	d := ns[0] ^ ns[1] ^ ns[2] ^ ns[3]
	for i := 0; i < 3; i++ {
		if ns[i+4] != d^ns[i] {
			return false
		}
	}
	return true
}

func p(ns []int) {
	for _, n := range ns {
		fmt.Printf("%d ", n)
	}
}

func main() {
	a, b := make([]int, 7, 7), make([]int, 7, 7)
	for i := 0; i < 7; i++ {
		fmt.Scan(&a[i])
	}
	if t(a) {
		p(a)
	} else {
		for i := 0; i < 7; i++ {
			copy(b, a)
			b[i] ^= 1
			if t(b) {
				p(b)
				return
			}
		}
	}
}

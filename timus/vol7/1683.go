package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	var ns []int
	for n > 1 {
		ns = append(ns, n/2)
		n = (n + 1) / 2
	}
	fmt.Println(len(ns))
	for _, i := range ns {
		fmt.Printf("%d ", i)
	}
}

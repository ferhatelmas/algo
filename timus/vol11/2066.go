package main

import (
	"fmt"
	"sort"
)

func main() {
	var a, b, c int
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	xs := []int{a - b*c, a - b + c, a - b - c}
	sort.Ints(xs)
	fmt.Println(xs[0])
}

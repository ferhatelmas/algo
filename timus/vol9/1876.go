package main

import "fmt"

func main() {
	var l, r int
	fmt.Scanf("%d %d", &l, &r)
	res := 39 * 3
	l -= 39
	r -= 39
	tl, tr := 2 + (l-1) * 2, 2 * r + 1
	if tl > tr {
		res += tl
	} else {
		res += tr
	}
	fmt.Println(res)
}
